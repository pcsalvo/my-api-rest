from django.db import models

# Create your models here.
class Albums(models.Model):
    album_id = models.CharField(max_length=22)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    artist = models.URLField(max_length=200)
    tracks = models.URLField(max_length=200)
    Self = models.URLField(max_length=200)

