from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.
class Answers(models.Model):
    question = models.CharField(max_length = 150)
    answer = models.CharField(max_length=150)
    timestamp = models.DateTimeField()

admin.site.register(Answers)