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

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.wordsmiths.models import WordType, Word, Sentence

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate User Data."""

    class Meta:
        """Nested Meta Class."""

        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Group Data."""

    class Meta:
        """Nested Meta Class."""

        model = Group
        fields = ['url', 'name']


class WordTypeSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Word Type Data."""

    class Meta:
        """Nested Meta Class."""
        model = WordType
        fields = ['name', 'created_by']


class WordSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Word Data."""

    class Meta:
        """Nested Meta Class."""
        model = Word
        fields = ['text', 'type', 'created_by']


class SentenceSerializer(serializers.HyperlinkedModelSerializer):
    """Class to validate Sentence Data."""

    class Meta:
        """Nested Meta Class."""
        model = Sentence
        fields = ['text', 'created_by']
