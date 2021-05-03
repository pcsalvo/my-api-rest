from django.db import models

# Create your models here.
class Tracks(models.Model):
    track_id = models.CharField(max_length=22)
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    times_played = models.IntegerField()
    artist = models.URLField(max_length=200)
    album = models.URLField(max_length=200)
    Self = models.URLField(max_length=200)

