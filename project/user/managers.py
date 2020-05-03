from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_superuser(self, email, password):

        # create new user
        user = self.model(
            email = email,
            password = password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
