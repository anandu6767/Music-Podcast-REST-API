from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, TrackTypeViewSet, SingerViewSet, AudioTrackViewSet

router = DefaultRouter()
router.register('albums', AlbumViewSet)
router.register('track-types', TrackTypeViewSet)
router.register('singers', SingerViewSet)
router.register('audio-tracks', AudioTrackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
