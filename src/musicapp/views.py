from django.shortcuts import render
from django.http import HttpResponse
from .models import Track, Author, Album
from django.db.models import Prefetch

# Create your views here.
def index(request):
    return render(request, 'index.html', {'index': index})


def albums(request):
    author_list = Author.objects.prefetch_related(Prefetch('albums', Album.objects.order_by('id'))).all()
    print(author_list.query)
    albums = {'author_list': author_list}
    return render(request, 'albums.html', albums)


def authors(request):
    return render(request, 'authors.html', {'authors': authors})


def playlist(request):
    return render(request, 'playlist.html', {'playlist': playlist})


def about(request):
    return render(request, 'about.html', {'about': about})


def news(request):
    return render(request, 'news.html', {'news': news})


def home(request):
    return render(request, 'home.html', {'home': home})


def get_album(request, album_id):
    album = Album.objects.select_related('author').filter(id=album_id)
    print(album.query)
    return render(request, 'album_detail.html', {'album': album.first()})