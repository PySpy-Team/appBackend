from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from .models import UserModel
from .helper import AuthenticateResult


def create_user(email, password):

    # create new user
    user = UserModel(
        email=email,
        password=password
    )

    # save user into DB
    user.set_password(password)
    user.save()

    # get user token
    token, _ = Token.objects.get_or_create(user=user)

    return token, user


def authenticate(email=None, password=None, create_new_user=False):

    try:
        # search for user
        user = UserModel.objects.get(email=email)
        print(user)

        print('pass: ', password)

        # validate entered password
        entered_password_is_valid = check_password(password, user.password)
        print('2', entered_password_is_valid)

        if entered_password_is_valid:
            # get a token for loggined user
            token, _ = Token.objects.get_or_create(user=user)
            print('1', token)

            result = AuthenticateResult(user, token)

            return result

        # return None for the case of wrong password
        return None

    except UserModel.DoesNotExist:

        if create_new_user:
            # return token for created user
            token, user = create_user(
                email=email, password=password
            )

            result = AuthenticateResult(user, token)

            return result

        return None
