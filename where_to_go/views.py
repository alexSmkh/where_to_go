from django.shortcuts import render
from django.urls import reverse
from places.models import Place


def show_main_page(request):
    features = []
    for place in Place.objects.all():
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('get_place', args=(place.id,))
            }
        })
    places = {
        'type': 'FeatureCollection',
        'features': features,
    }

    context = {'places': places}

    return render(request, 'index.html', context)
