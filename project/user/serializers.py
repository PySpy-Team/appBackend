from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'xp', 'is_superuser']

        validators = [
            UniqueTogetherValidator(
                queryset = UserModel.objects.all(),
                fields=['email']
            )
        ]

        extra_kwargs = {
             'username': {'required': False}
        }