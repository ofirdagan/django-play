from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name