from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from user import helper as user_helper
from . import helper as challenge_helper

from .models import ChallengeModel, StoreUserAnswer
from . import serializers


@api_view(['GET'])
@user_helper.login_required
def get_challenge(request, user, id):

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
@challenge_helper.memorize_user_answer
def get_answers(request, user, challenge, id):

    try:
        # update user's xp
        data = user_helper.get_data(request)

        user_choice = filter(
            lambda item: item["id"] == data["id"],
            challenge.choices.values()
        )

        user_choice = list(user_choice)
        print(user_choice)

        out_of_choices = lambda data: len(data) == 0

        if out_of_choices:
            return Response(
                user_helper.message('choice index out of range.'),
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        # user should send choice ID
        for choice in challenge.choices.values():
            if data['id'] == choice['id']:
                if choice['is_correct']:
                    # update user's xp
                    user.xp += challenge.score
                    user.save()

        # save user answer
        storage = StoreUserAnswer(
            user=user,
            challenge=challenge,
            choice=user_choice[0]
        )

        answers = serializers.AnswerSerializer(challenge)

        result = {
            **answers.data,
            'current_xp': user.xp
        }

        return Response(
            result,
            status=status.HTTP_200_OK
        )

    except Exception as err:

        print(err)

        return Response(
            user_helper.message('challenge not found'),
            status=status.HTTP_404_NOT_FOUND
        )
