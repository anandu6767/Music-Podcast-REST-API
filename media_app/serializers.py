from rest_framework import serializers
from .models import Album, TrackType, Singer, AudioTrack

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class TrackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackType
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'

class AudioTrackSerializer(serializers.ModelSerializer):
    singers = serializers.StringRelatedField(many=True)
    album = AlbumSerializer()
    track_type = TrackTypeSerializer()
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.added_by.first_name or obj.added_by.username

    class Meta:
        model = AudioTrack
        fields = '__all__'

class AudioTrackCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioTrack
        fields = '__all__'

    def validate(self, data):
        track_type = data.get('track_type')
        album = data.get('album')
        if track_type and track_type.name == "Song" and not album:
            raise serializers.ValidationError("Album is mandatory for Songs.")
        return data
