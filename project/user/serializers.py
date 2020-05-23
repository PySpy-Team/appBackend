from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import UserModel
from challenge.models import ChallengeModel

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'xp', 'is_staff']

        validators = [
            UniqueTogetherValidator(
                queryset = UserModel.objects.all(),
                fields=['email']
            )
        ]

        extra_kwargs = {
             'username': {'required': False}
        }

class ChallengeHeaderSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    score = serializers.IntegerField()