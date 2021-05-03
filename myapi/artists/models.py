from django.db import models

# Create your models here.
class Artists(models.Model):
    artist_id = models.CharField(max_length=22)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    albums = models.URLField(max_length=200)
    tracks = models.URLField(max_length=200)
    Self = models.URLField(max_length=200)

