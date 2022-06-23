from django.shortcuts import render
from .models import Track, Author, Album


# Create your views here.
def index(request):
    author_list = Author.objects.all()
    context = {'author_list': author_list}
    return render(request, 'index.html', context)
