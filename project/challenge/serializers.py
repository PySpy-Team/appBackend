from rest_framework import serializers
from .models import ChallengeModel, ChoiceModel
from user.models import UserModel


class ChoiceHeader(serializers.ModelSerializer):
    class Meta():
        model = ChoiceModel
        fields = [
            'id',
            'body'
        ]

class Answer(serializers.ModelSerializer):
    class Meta():
        model = ChoiceModel
        fields = [
            'id',
            'is_correct'
        ]

class AnswerSerializer(serializers.ModelSerializer):
    choices = Answer(read_only=True, many=True)

    class Meta():
        model = ChallengeModel
        fields = ['choices']



class Author(serializers.ModelSerializer):
    class Meta():
        model = UserModel
        fields = [
            'id',
            'username',
            'profile'
        ]

class ChallengeSerializer(serializers.ModelSerializer):
    author = Author()
    choices = ChoiceHeader(many=True, read_only=True)

    class Meta():
        model = ChallengeModel
        fields = [
            'author',
            'title',
            'content',
            'score',
            'choices'
        ]


class ChallengeHeaderSerializer(serializers.ModelSerializer):
    author = Author()

    class Meta():
        model = ChallengeModel
        fields = [
            'id',
            'author',
            'title',
            'score'
        ]

