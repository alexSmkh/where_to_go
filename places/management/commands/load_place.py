import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand, CommandError
from places.models import Place, PlaceImage


def create_place_image(place, place_image_url, image_filename):
    response = requests.get(place_image_url)
    response.raise_for_status()

    content_file = ContentFile(response.content, name=image_filename)

    PlaceImage.objects.create(place=place, image=content_file)


def create_place(place):
    place_entry, created = Place.objects.get_or_create(
        title=place['title'],
        defaults={
            'description_short': place.get('description_short', ''),
            'description_long': place.get('description_long', ''),
            'longitude': place['coordinates']['lng'],
            'latitude': place['coordinates']['lat']
        }
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
            response = requests.get(file_url)
            response.raise_for_status()
            create_place(response.json())
        except requests.exceptions.HTTPError:
            raise CommandError('Something went wrong. Check the file url and try again.')
        except requests.exceptions.ConnectionError:
            raise CommandError('Internet connection problems. Please try again later.')
        except requests.exceptions.JSONDecodeError:
            raise CommandError('You provided the wrong link. The link should lead to a json file.')
