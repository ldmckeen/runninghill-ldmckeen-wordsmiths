"""
Runninghill Wordsmiths API Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<urls.py> DRF App url's File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Runninghill
Date:               February 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.wordsmiths import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'groups', views.UserViewSet, basename='group')
router.register(r'word_type', views.WordTypeViewSet, basename='word_type')
router.register(r'words', views.WordViewSet, basename='word')
router.register(r'sentences', views.SentenceViewSet, basename='sentence')

# API endpoints
urlpatterns = [
    path('', include(router.urls)),
]
