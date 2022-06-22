from django.shortcuts import render
from .models import Track, Author, Album


# Create your views here.
def index(request):
    tracklist = Track.objects.all()
    return render(request, 'index.html', {'tracklist': tracklist})


def author(request):
    author = Author.objects.all()
    album = Album.objects.all()
    context = {'author': author, 'album': album}
    return render(request, 'index.html', context)
