from django.db import models

class PatternChoices(models.Choices):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    DIAGONAL = "diagonal"

