from django.shortcuts import render
from .models import Track, Author, Album


# Create your views here.
def index(request):
    author_list = Author.objects.all()
    context = {'author_list': author_list}
    return render(request, 'index.html', context)


def albums(request):
    author_list = Author.objects.all()
    albums = {'author_list': author_list}
    return render(request, 'albums.html', albums)


def authors(request):
    return render(request, 'authors.html', {'authors': authors})


def musiclabel(request):
    return render(request, 'musiclabel.html', {'musiclabel': musiclabel})


def playlist(request):
    return render(request, 'playlist.html', {'playlist': playlist})


def about(request):
    return render(request, 'about.html', {'about': about})


def news(request):
    return render(request, 'news.html', {'news': news})
