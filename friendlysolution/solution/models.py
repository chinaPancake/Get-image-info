from enum import unique
from django.db import models
from django.forms import ModelForm
# Create your models here.

class ImageInfo(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=255)
    albumId = models.IntegerField
    url = models.IntegerField()
