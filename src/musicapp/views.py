from django.shortcuts import render
from .models import Track
# Create your views here.
def index(request):
    tracklist = Track.objects.all()
    print(tracklist.query)
    return render(request, 'index.html', {'tracklist':tracklist})