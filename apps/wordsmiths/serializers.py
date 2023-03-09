"""
Runninghill Wordsmiths API Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<serializers.py> DRF Serializers File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Runninghill
Date:               February 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================

"""
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.wordsmiths.models import Sentence
from apps.wordsmiths.models import Word
from apps.wordsmiths.models import WordType


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate User Data."""

    class Meta:
        """Nested Meta Class."""

        model = User
        fields = ['url', 'id', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Group Data."""

    class Meta:
        """Nested Meta Class."""

        model = Group
        fields = ['url', 'id', 'name']


class WordTypeSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Word Type Data."""
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=False)

    class Meta:
        """Nested Meta Class."""
        model = WordType
        fields = ['url', 'id', 'name', 'created_by']


class SentenceSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Sentence Data."""
    words = serializers.PrimaryKeyRelatedField(
        queryset=Word.objects.all(), many=True)
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=False)

    class Meta:
        """Nested Meta Class."""
        model = Sentence
        fields = ['url', 'id', 'words', 'text', 'created_by']
        extra_kwargs = {
            'text': {'read_only': True},
            'words': {'required': False}
        }


class WordSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Word Data."""
    sentences = SentenceSerializer(many=True, read_only=True)
    type = serializers.PrimaryKeyRelatedField(
        queryset=WordType.objects.all(), many=False)
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=False)

    class Meta:
        """Nested Meta Class."""
        model = Word
        fields = ['url', 'id', 'name', 'type', 'created_by', 'sentences']
        extra_kwargs = {
            'sentences': {'required': False}
        }
