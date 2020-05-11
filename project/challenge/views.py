from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from user import helper

from .models import ChallengeModel
from . import serializers

@api_view(['GET'])
@helper.login_required
def get_challenge(request, user, id):
    
    # try to find the challenge.
    try:
        challenge = ChallengeModel.objects.get(pk = id)
        
        serializer = serializers.ChallengeSerializer(challenge)
        
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )

    except Exception as error:

        print(error)

        return Response(
            helper.message('challenge not found'),
            status = status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
@helper.login_required
def get_answers(request, user, id):
    
    try:
        challenge = ChallengeModel.objects.get( pk = id )
        answers = serializers.AnswerSerializer(challenge)

        return Response(
            answers.data,
            status = status.HTTP_200_OK
        )

    except Exception as err:
        
        print(err)

        return Response(
            helper.message('challenge not found'),
            status = status.HTTP_404_NOT_FOUND 
        )