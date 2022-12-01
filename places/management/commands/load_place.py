import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand, CommandError
from places.models import Place, PlaceImage


def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def create_place_image(place, place_image_url, image_filename):
    place_image = PlaceImage(place=place)
    response = fetch_data(place_image_url)
    place_image.image.save(image_filename, ContentFile(response.content))


def create_place(place):
    place_entry, created = Place.objects.get_or_create(
        title=place['title'],
        description_short=place.get('description_short', ''),
        description_long=place.get('description_long', ''),
        longitude=place['coordinates']['lng'],
        latitude=place['coordinates']['lat']
    )

    if not created:
        return

    for num, image_url in enumerate(place.get('imgs', []), start=1):
        image_filename = f'{num}_{place["title"]}.jpg'
        create_place_image(place_entry, image_url, image_filename)


class Command(BaseCommand):
    help = 'Load place from json file'

    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--url',
            required=True
        )

    def handle(self, *args, **options):
        file_url = options['url']

        try:
            create_place(fetch_data(file_url).json())
        except requests.exceptions.HTTPError:
            raise CommandError('Something went wrong. Check the file url and try again.')
        except requests.exceptions.ConnectionError:
            raise CommandError('Internet connection problems. Please try again later.')
        except requests.exceptions.JSONDecodeError:
            raise CommandError('You provided the wrong link. The link should lead to a json file.')
