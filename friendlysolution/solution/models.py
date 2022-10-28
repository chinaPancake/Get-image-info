from enum import unique
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your models here.

class ImageInfoo(models.Model):
    id = models.AutoField(primary_key = True)
    photo_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    albumId = models.IntegerField(null = True)
    width = models.IntegerField(null = True)
    height = models.IntegerField(null = True)
    dominantcolor = models.CharField(max_length=10)
    url = models.CharField(max_length=255)