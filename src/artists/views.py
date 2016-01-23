from django.shortcuts import render

from rest_framework import viewsets
from .models import Artist
from albums.models import Album
from .serializers import ArtistSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status
import urllib2
import logging
import json

logger = logging.getLogger(__name__)

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.order_by('-created_at')
    serializer_class = ArtistSerializer

    # @detail_route(methods=['get'], url_path='bla')
    def create(self, request):
        name = request.data['name']
        itunesUrl = "https://itunes.apple.com/search?term={artist}&media=music&entity=album&limit=2".format(artist=urllib2.quote(name))
        result = urllib2.urlopen(itunesUrl).read()
        albums = json.loads(result)

        if albums["resultCount"] == 0:
            return Response({'success': False}, status=status.HTTP_204_NO_CONTENT)
        else:
            artist = Artist(name=name)
            artist.save()
            for album in albums["results"]:
                album = Album(name=album["collectionName"], imageUrl=album["artworkUrl100"], artist=artist)
                album.save()

            return Response({'success': True, 'artist': name, 'results': albums['resultCount']}, status=status.HTTP_201_CREATED)