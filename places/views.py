from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from .models import Place


def get_place(request, pk):
    place_entry = get_object_or_404(Place, pk=pk)
    place_image_urls = list(map(
        lambda image: request.build_absolute_uri(image.image.url),
        place_entry.images.all()
    ))

    place = {
        'title': place_entry.title,
        'description_short': place_entry.description_short,
        'description_long': place_entry.description_long,
        'coordinates': {
            'lat': place_entry.coordinate_lat,
            'lng': place_entry.coordinate_lng,
        },
        'imgs': place_image_urls
    },

    return JsonResponse(
        place,
        safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2,
        },
    )


