from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import UserModel

class AuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):

        try:
            user = UserModel.objects.get(email=email)
            entered_password_is_valid = check_password(password, user.password)

            if entered_password_is_valid:
                return user

            return None

        except UserModel.DoesNotExist:
            return None