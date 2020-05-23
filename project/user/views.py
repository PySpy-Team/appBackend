from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


# reading POST data.
from .helper import (
    get_data,
    message,
    login_required
)

# login & singup
from .auth import authenticate
from .serializers import UserModelSerializer, ChallengeHeaderSerializer
from .models import UserModel


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

    print(auth)

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
        print('update username')
        user.username = data['username']

    # update password
    if 'password' in data:
        # store hashed password
        print('update password')
        user.set_password(data['password'])

    # update user with new data
    user.save()
    print(user)

    serilizer = UserModelSerializer(user)

    response = Response(
        data=serilizer.data,
        status=status.HTTP_200_OK
    )

    return response


@api_view(['GET'])
@login_required
def get_user_challenges( request, user: UserModel ):

    try:
        challenges = user.challenges
        serilizer = ChallengeHeaderSerializer(
            challenges.all(),
            many = True
        )

        return Response(
            serilizer.data,
            status=status.HTTP_200_OK
        )

    except Exception as err:
        print(err)

        return Response(
            message('something is wrong.'),
            status = status.HTTP_500_INTERNAL_SERVER_ERROR
        )
