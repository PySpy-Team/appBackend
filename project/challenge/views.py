from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from user import helper as user_helper
from user.models import UserModel
from . import helper as challenge_helper

from .models import ChallengeModel, StoreUserAnswer, ChoiceModel
from . import serializers


@api_view(['GET'])
@user_helper.login_required
def get_challenge(request, user: UserModel, id: int):

    # try to find the challenge.
    try:
        challenge = ChallengeModel.objects.get(pk=id)

        serializer = serializers.ChallengeSerializer(challenge)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    except Exception as error:

        print(error)

        return Response(
            user_helper.message('challenge not found'),
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
@user_helper.login_required
def create_challenge(request, user: UserModel):

    data = user_helper.get_data(request)

    # serializer also will look for author
    # author is a instance from UserModel
    # in the form of Dictionary
    author = serializers.Author(user)
    data['author'] = author.data


    new_challenge = serializers.ChallengeSerializer(
        data = data
    )

    if new_challenge.is_valid():

        # first save all choices
        choices = challenge_helper.save_choices(
            choices = data['choices']
        )

        # save the challenge
        challenge = ChallengeModel(
            author = user,
            title = data['title'],
            content = data['content'],
            score = data['score']
        )

        challenge.save()

        # add all choices to challenge
        for choice in choices:
            challenge.choices.add(choice)

        # add challenge to user's list
        user.challenges.add(challenge)

        serilizer = serializers.ChallengeHeaderSerializer(challenge)

        return Response(
            data = serilizer.data,
            status = status.HTTP_201_CREATED
        )


    return Response(
        data = user_helper.message('invalid fields'),
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@user_helper.login_required
# this decorator won't let user to answer twice
@challenge_helper.memorize_user_answer
def get_answers(request, user, challenge, id):

    try:
        # get POST data
        data = user_helper.get_data(request)

        # check wich one of choices choosen.
        user_choice = filter(
            lambda item: item["id"] == data["id"],
            challenge.choices.values()
        )

        # convert filter object to list
        user_choice = list(user_choice)


        # the case which user choice was out of avaible choices
        # the choice id does not belongs to any of choies.
        out_of_choices = len( user_choice ) == 0

        if out_of_choices:
            return Response(
                user_helper.message('choice index out of range.'),
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        # check if user choosen correct choice
        # then increase user's xp 
        for choice in challenge.choices.values():
            if data['id'] == choice['id']:
                if choice['is_correct']:
                    # update user's xp
                    user.xp += challenge.score
                    user.save()

        # save user answer
        # next time @memorize_user_answer
        # wont let user to answer this challenge again

        # user_choice is correcntly a dic object
        # it should be ChoiceModel instance
        user_choice = ChoiceModel.objects.get(
            pk = user_choice[0]['id']
        )

        storage = StoreUserAnswer(
            user = user,
            challenge = challenge,
            choice = user_choice
        )

        # save into DB
        storage.save()

        answers = serializers.AnswerSerializer(challenge)

        result = {
            ** answers.data,
            'current_xp': user.xp
        }
 
        return Response(
            result,
            status=status.HTTP_200_OK
        )

    except:

        return Response(
            user_helper.message('challenge not found'),
            status=status.HTTP_404_NOT_FOUND
        )
