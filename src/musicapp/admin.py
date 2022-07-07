from django.contrib import admin
from .models import Track, Author, Album, PlayList, MusicLabel

# Register your models here.
admin.site.register(Track)
admin.site.register(Author)
admin.site.register(Album)
admin.site.register(PlayList)

