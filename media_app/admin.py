from django.contrib import admin
from .models import Album, TrackType, Singer, AudioTrack

admin.site.register(Album)
admin.site.register(TrackType)
admin.site.register(Singer)
admin.site.register(AudioTrack)
