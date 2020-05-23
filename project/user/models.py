from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
import random, string

# Token auth stuff.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# each user has it's own image folder
# user with primary key 1 will get stored in /user_1/image.png
def user_image_path(self, filename):
    return 'upload/user_{0}/{1}'.format(self.id, filename) 

class UserModel(
        AbstractBaseUser,
        PermissionsMixin
    ):
    # by default email field in django's User model is optional
    # we need to define our email field to be unique and required

    username = models.CharField(max_length=200)

    # email field should be unique, and immutable
    email = models.EmailField(unique=True)
    xp = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)

    # each challenge has author field
    # which relate to UserModel
    # also each user has it's challenge list
    challenges = models.ManyToManyField(
        "challenge.ChallengeModel"
    )

    REQUIRED_FIELDS = []
    # auth will be based on email
    USERNAME_FIELD = "email"


    objects = UserManager()

    def __str__(self):
        return f"{self.email} : {self.username}"

    def save(self, *args, **kwargs):

        # generate random name if username field is empty
        # e.g. : user KFDX
        if self.username == "" or self.username == None:
            # generate random string
            userID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

            # update field with generated name
            self.username = f"user {userID}"

        super(UserModel, self).save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)