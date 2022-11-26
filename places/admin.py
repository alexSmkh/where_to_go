from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    readonly_fields = ('place_images',)
    model = PlaceImage

    def place_images(self, place_image):
        return format_html('<img src="{}" height="{}"', place_image.image.url, '200px')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
