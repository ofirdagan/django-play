from rest_framework import serializers
from artists.serializers import ArtistSerializer
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True, required=False)

    class Meta:
        model = Album
        fields = ('id', 'name', 'imageUrl', 'releaseDate', 'artist')
