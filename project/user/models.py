from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import random, string

# each user has it's own image folder
# user with primary key 1 will get stored in /user_1/image.png
def user_image_path(self, filename):
    return 'upload/user_{0}/{1}'.format(self.id, filename) 

class UserModel(AbstractBaseUser):
    # by default email field in django's User model is optional
    # we need to define our email field to be unique and required

    username = models.CharField(max_length=200)

    #email field should be unique, and immutable
    email = models.EmailField(unique=True)
    profile = models.ImageField(upload_to=user_image_path, default='upload/default.png')
    xp = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    # auth will be based on email
    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):

        # generate random name if username field is empty
        # e.g. : user KFDX
        if self.username == "" or self.username == None:
            # generate random string
            userID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

            # update field with generated name
            self.username = f"user {userID}"

        # encrypt password
        self.set_password(self.password)

        super(UserModel, self).save(*args, **kwargs)



    