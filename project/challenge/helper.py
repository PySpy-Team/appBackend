from rest_framework.response import Response
from rest_framework import status
from user import helper
from .models import StoreUserAnswer, ChallengeModel

def memorize_user_answer(func):

    def decorator(request, user, id, *args, **kwargs):
 
        try:
            # check if challenge exist
            challenge = ChallengeModel.objects.get(pk=id)

        except ChallengeModel.DoesNotExist:

            return Response (
                helper.message('challenge not found'),
                status=status.HTTP_404_NOT_FOUND
            )

        # now check if user already answered.
        # it will raise an erro if doesn't exist
        try:
            user_answered = StoreUserAnswer.objects.get(
                user = user, 
                challenge = challenge
            )

            return Response(
                helper.message('user already answered this challenge.'),
                status = status.HTTP_403_FORBIDDEN
            )

        except StoreUserAnswer.DoesNotExist:

            return func(request, user, challenge, id, *args, **kwargs)

    return decorator