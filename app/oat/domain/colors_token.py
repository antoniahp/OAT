from django.db import models

from config import settings
from oat.domain.color_choices import ColorChoices
from oat.domain.pattern_choices import PatternChoices


class ColorsToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_color = models.CharField(max_length=256, choices=ColorChoices.choices)
    second_color = models.CharField(max_length=256, choices=ColorChoices.choices)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    pattern = models.CharField(max_length=256, choices=PatternChoices.choices)
