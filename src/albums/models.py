from __future__ import unicode_literals

from django.db import models
from artists.models import Artist

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255, blank=False)
    imageUrl = models.URLField()
    releaseDate = models.DateTimeField(null=True)
    artist = models.ForeignKey(Artist)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name