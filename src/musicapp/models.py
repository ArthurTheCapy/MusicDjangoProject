from django.db import models


# def user_directory_path(instance, filename):
#    return 'user_{0}/{1}'.format(instance.user.id, filename)


# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()


class Author(models.Model):
    band_name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)


class Album(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    # album_picture = models.FileField(upload_to=user_directory_path)
    album_release = models.CharField(max_length=100)
    num_stars = models.IntegerField()


class PlayList(models.Model):
    playlist_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    song = models.ForeignKey(Track, on_delete=models.CASCADE)


class MusicLabel(models.Model):
    label_name = models.CharField(max_length=100)
    label_description = models.CharField(max_length=100)
