from django.shortcuts import render

from places.models import Place


def show_main_page(request):
    features = []
    for place in Place.objects.all():
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coordinate_lng, place.coordinate_lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": {
                    "title": place.title,
                    "description_short": place.description_short,
                    "description_long": place.description_long,
                    "coordinates": {
                        "lat": place.coordinate_lat,
                        "lng": place.coordinate_lng
                    }
                }
            }
        })
    places = {
        "type": "FeatureCollection",
        "features": features,
    }

    context = {'places': places}

    return render(request, 'index.html', context)
