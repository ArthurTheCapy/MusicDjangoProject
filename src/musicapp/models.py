from django.db import models


# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


class Author(models.Model):
    band_name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.band_name


class Album(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="albums")
    name = models.CharField(max_length=100)
    label = models.ForeignKey("MusicLabel", on_delete=models.CASCADE, null=True, blank=True)
    cover = models.FileField(upload_to='covers', null=True, blank=True)
    release_date = models.DateField()
    num_stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class PlayList(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    song = models.ForeignKey(Track, on_delete=models.CASCADE)


class MusicLabel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
