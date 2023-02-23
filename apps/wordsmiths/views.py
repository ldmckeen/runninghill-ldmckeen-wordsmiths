"""
Runninghill Wordsmiths API Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<views.py> DRF Views File

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
from rest_framework import permissions
from rest_framework import viewsets

from apps.wordsmiths.models import Sentence
from apps.wordsmiths.models import Word
from apps.wordsmiths.models import WordType
from apps.wordsmiths.serializers import GroupSerializer
from apps.wordsmiths.serializers import SentenceSerializer
from apps.wordsmiths.serializers import UserSerializer
from apps.wordsmiths.serializers import WordSerializer
from apps.wordsmiths.serializers import WordTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class WordTypeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows APScanData to be viewed or edited."""

    queryset = WordType.objects.all()
    serializer_class = WordTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WordViewSet(viewsets.ModelViewSet):
    """API endpoint that allows APScanData to be viewed or edited."""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SentenceViewSet(viewsets.ModelViewSet):
    """API endpoint that allows APScanData to be viewed or edited."""

    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
