from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=100, help_text='Название')
    description_short = models.CharField(max_length=1000, help_text='Короткое описание')
    description_long = tinymce_models.HTMLField(max_length=10000, help_text='Полное описание')
    coordinate_lng = models.FloatField(help_text='Координаты(долгота)')
    coordinate_lat = models.FloatField(help_text='Координаты(широта)')
    created_at = models.DateTimeField(help_text='Дата создания')
    updated_at = models.DateTimeField(blank=True, null=True, help_text='Дата обновления')
    published_at = models.DateTimeField(blank=True, null=True, help_text='Дата публикации')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', related_query_name='image')
    image = models.ImageField(upload_to='place_images')
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False, db_index=True)

    class Meta:
        ordering = ['order']
