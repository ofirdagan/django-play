from django.contrib import admin

# Register your models here.
from .models import Album
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "created_at", "updated_at", "artist"]
    class Meta:
        model = Album


admin.site.register(Album, AlbumAdmin)