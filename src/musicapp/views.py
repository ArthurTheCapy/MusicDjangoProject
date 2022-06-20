from django.shortcuts import render
from .models import Track, Author, Album


# Create your views here.
def index(request):
    tracklist = Track.objects.all()
    print(tracklist.query)
    return render(request, 'index.html', {'tracklist': tracklist})


def index(request):
    author = Author.objects.all()
    print(author.query)
    return render(request, 'index.html', {'author': author})


def index(request):
    album = Album.objects.all()
    print(album.query)
    return render(request, 'index.html', {'albums': album})
