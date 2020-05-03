from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

# reading POST data.
from .helper import get_data

# login & singup
from django.contrib.auth import authenticate
from .serializers import UserModelSerializer


@csrf_exempt
@api_view(['POST'])
def singup(request, format=None):

    # convert json data into dictionary
    data = get_data(request)

    #push POST data into serializer 
    serializer = UserModelSerializer(
        data = data
    )

    # validate POST data
    if serializer.is_valid():

        # add new user
        auth = authenticate(
            email = data['email'],
            password = data['password'],
            create_new_user = True
        )

        # save user's token on session
        # next time user tagged as authenticated
        request.session['token'] = auth.token.key

        # convert user object into json object
        user = UserModelSerializer(auth.user)

        return Response(
            user.data,
            status = status.HTTP_200_OK
        )

    else:

        error_message = {
            "message": "invalid data."
        }

        return Response(
            error_message,
            status = status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def login(request):

    # convert json data into dictionary
    data = get_data(request)

    auth = authenticate(
        email = data['email'],
        password = data['password']
    )

    if auth:
        # store user's token into sesion
        request.session['token'] = auth.token.key

        user = UserModelSerializer(auth.user)

        return Response(
            user.data,
            status = status.HTTP_200_OK
        )

    else:
        # return error message if authentication failed
        error_message = {
            "message": "user doesn't exist or wrong password"
        }

        return Response(
            error_message,
            status = status.HTTP_403_FORBIDDEN
        )