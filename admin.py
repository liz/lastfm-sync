from django.contrib import admin
from models import *


class LastFmAdmin(admin.ModelAdmin):
  list_display = ('pub_date', 'chart', 'artist', 'track', 'album')
  list_filter = ('pub_date', 'chart', 'artist', 'album')

admin.site.register(LastfmPost, LastFmAdmin)