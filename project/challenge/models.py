from django.db import models
from user.models import UserModel

class ChoiceModel(models.Model):
    body = models.CharField(max_length = 200)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.body

class ChallengeModel(models.Model):
    author = models.ForeignKey(UserModel, null=True, on_delete = models.SET_NULL)
    title = models.CharField(max_length = 200, unique=True)
    content = models.TextField()
    score = models.IntegerField()

    choices = models.ManyToManyField( ChoiceModel )

    def __str__(self):
        return f"{self.title} : {self.score}"

class StoreUserAnswer(models.Model):
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    challenge = models.ForeignKey(ChallengeModel, on_delete = models.CASCADE)
    choice = models.ForeignKey(ChoiceModel, on_delete = models.CASCADE)