from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response


class ArtistAlbumsViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer

    def list(self, request, artist_pk=None):
        queryset = Album.objects.filter(artist__id=artist_pk)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
        # return Response({})
