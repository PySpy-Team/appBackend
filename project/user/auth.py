from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from .models import UserModel
from .helper import AuthenticateResult

def create_user(email, password):

    # create new user
    user = UserModel(
        email = email,
        password = password
    )

    # save user into DB
    user.save()

    # get user token
    token, _ = Token.objects.get_or_create(user=user)

    return token, user

class AuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, create_new_user=False):

        try:
            # search for user
            user = UserModel.objects.get(email=email)

            # validate entered password
            entered_password_is_valid = check_password(password, user.password)

            if entered_password_is_valid:
                # get a token for loggined user
                token, _ = Token.objects.get_or_create(user=user)
                
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
            