from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from .models import Place


def get_place(request, pk):
    place_entry = get_object_or_404(Place, pk=pk)

    place = {
        'title': place_entry.title,
        'description_short': place_entry.description_short,
        'description_long': place_entry.description_long,
        'coordinates': {
            'lat': place_entry.latitude,
            'lng': place_entry.longitude,
        },
        'imgs': [image.image.url for image in place_entry.images.all()]
    }

    return JsonResponse(place, json_dumps_params={'ensure_ascii': False})


