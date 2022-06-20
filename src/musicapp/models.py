from django.db import models


# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    band_name = models.CharField(max_length=50)


class Album(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class PlayList(models.Model):
    playlist_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    song = models.ForeignKey(Track, on_delete=models.CASCADE)


class MusicLabel(models.Model):
    label_name = models.CharField(max_length=100)
    label_date = models.DateField()
