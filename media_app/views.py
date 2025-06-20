from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .models import Album, TrackType, Singer, AudioTrack
from .serializers import (
    AlbumSerializer, TrackTypeSerializer, SingerSerializer,
    AudioTrackSerializer, AudioTrackCreateUpdateSerializer
)
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class AlbumViewSet(BaseViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackTypeViewSet(BaseViewSet):
    queryset = TrackType.objects.all()
    serializer_class = TrackTypeSerializer

class SingerViewSet(BaseViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class AudioTrackViewSet(BaseViewSet):
    queryset = AudioTrack.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AudioTrackCreateUpdateSerializer
        return AudioTrackSerializer

    def get_queryset(self):
        queryset = AudioTrack.objects.select_related('album', 'track_type', 'added_by').prefetch_related('singers')
        singer_id = self.request.query_params.get('singer')
        album_id = self.request.query_params.get('album')

        if singer_id:
            queryset = queryset.filter(singers__id=singer_id)
        if album_id:
            queryset = queryset.filter(album__id=album_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
