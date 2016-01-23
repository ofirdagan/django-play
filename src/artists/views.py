from django.shortcuts import render

from rest_framework import viewsets
from .models import Artist
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
        url = "https://itunes.apple.com/search?term=%(artist)&media=music&entity=album".format(artist=name)
        albums = urllib2.urlopen(url).read()
        jsonObj = json.loads(albums)

        logger.error(albums)
        return Response({'artist': name, 'results': jsonObj['resultCount']}, status=status.HTTP_201_CREATED)