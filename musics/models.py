from unicodedata import name
from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
