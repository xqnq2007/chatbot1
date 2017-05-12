from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    q = models.CharField(max_length = 150)
    a = models.CharField(max_length = 150)
    timestamp = models.DateTimeField()
