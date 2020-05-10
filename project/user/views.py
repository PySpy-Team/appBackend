from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

# reading POST data.
from .helper import (
    get_data,
    message,
    login_required
)

# login & singup
from .auth import authenticate
from .serializers import UserModelSerializer


@csrf_exempt
@api_view(['POST'])
def singup(request, format=None):

    # convert json data into dictionary
    data = get_data(request)

    # push POST data into serializer
    serializer = UserModelSerializer(
        data=data
    )

    # validate POST data
    if serializer.is_valid():

        # add new user
        auth = authenticate(
            email=data['email'],
            password=data['password'],
            create_new_user=True
        )

        # save user's token on cookies
        # next time user tagged as authenticaten

        # convert user object into json object
        user = UserModelSerializer(auth.user)

        response = Response(
            user.data,
            status=status.HTTP_200_OK
        )

        response.set_cookie('token', auth.token.key)
        return response

    else:

        return Response(
            message("validation failed"),
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def login(request):

    # convert json data into dictionary
    data = get_data(request)

    auth = authenticate(
        email=data['email'],
        password=data['password']
    )

    if auth:
        # store user's token into client's cookie
        user = UserModelSerializer(auth.user)

        response = Response(
            user.data,
            status=status.HTTP_200_OK
        )

        response.set_cookie('token', auth.token.key)
        return response

    else:

        return Response(
            message("user doestn't exist | incorrect password"),
            status=status.HTTP_403_FORBIDDEN
        )


@api_view(['POST'])
@login_required
def update(request, user):

    data = get_data(request)

    # update username
    if 'username' in data:
        user.username = data['username']

    # update password 
    if 'password' in data:
        # store hashed password
        user.set_password( data['password'] )

    # update user with new data
    user.save()

    serilizer = UserModelSerializer(user)

    return Response(
        data = serilizer.data,
        status = status.HTTP_200_OK
    )