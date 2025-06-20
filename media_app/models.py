from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    name = models.CharField(max_length=100)
    released_on = models.DateTimeField()

    def __str__(self):
        return self.name

class TrackType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Singer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AudioTrack(models.Model):
    name = models.CharField(max_length=100)
    singers = models.ManyToManyField(Singer)
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.SET_NULL)
    length = models.CharField(max_length=10)
    track_type = models.ForeignKey(TrackType, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
