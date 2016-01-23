from django.contrib import admin

# Register your models here.
from .models import Artist
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "created_at", "updated_at"]
    class Meta:
        model = Artist


admin.site.register(Artist, ArtistAdmin)