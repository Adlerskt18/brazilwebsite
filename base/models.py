from django.db import models

# Create your models here.

class Matches(models.Model):

    date = models.CharField(("Date"), max_length=255)
    match = models.CharField(("Match"), max_length=255)
    result = models.CharField(("Result"), max_length=255)
    score = models.CharField(("Score"), max_length=255)
    competition = models.CharField(("Competition"), max_length=255)

        