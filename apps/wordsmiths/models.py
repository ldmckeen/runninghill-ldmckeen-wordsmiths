"""
Runninghill Wordsmiths API Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<models.py> DRF Models Class File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Runninghill
Date:               February 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""

from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel


WORD_TYPE = [
    ('noun', 'Noun'),
    ('verb', 'Verb'),
    ('adjective', 'Adjective'),
    ('adverb', 'Adverb'),
    ('pronoun', 'Pronoun'),
    ('preposition', 'Preposition'),
    ('conjunction', 'Conjunction'),
    ('determiner', 'Determiner'),
    ('exclamation', 'Exclamation')
]


class WordType(TimeStampedModel):
    """Type of English word."""

    name = models.CharField(choices=WORD_TYPE, max_length=11, default=None, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Provide human readable representation."""
        return self.type


class Word(TimeStampedModel):
    """Word object consisting of text characters and type."""

    text = models.CharField('English Word ', max_length=500)
    type = models.ForeignKey(WordType, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Provide human readable representation."""
        return self.text


class Sentence(TimeStampedModel):
    """Sentence object comprised of words with type."""

    text = models.CharField('English Sentence ', max_length=5000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

