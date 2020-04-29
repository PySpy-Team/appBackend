from django.db import models
from django.contrib.auth.models import User as BaseUser

import random, string

class User(BaseUser):
    # by default email field in django's User model is optional
    # we define it as a required field
    email = models.EmailField(unique=True, blank=True)
    xp = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        # generate random name if username field is empty
        # e.g. : user KFDX
        if self.username == "" or self.username == None:
            # generate random string
            userID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

            # update field with generated name
            self.username = f"user {userID}"

        super(User, self).save(*args, **kwargs)

    