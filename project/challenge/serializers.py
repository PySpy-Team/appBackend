from rest_framework import serializers
from .models import ChallengeModel, ChoiceModel

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta():
        model = ChallengeModel
        fields = [
            'author',
            'title',
            'content',
            'score'
        ]


class Choice(serializers.ModelSerializer):
    class Meta():
        model = ChoiceModel
        fields = [
            'body',
            'is_correct'
        ]

class ChoiceSerializer(serializers.ModelSerializer):
    choices = Choice(read_only=True, many=True)

    class Meta():
        model = ChallengeModel
        fields = ['choices']