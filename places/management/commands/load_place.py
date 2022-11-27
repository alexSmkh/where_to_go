import json
import os.path

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand, CommandError
from places.models import Place, PlaceImage


def create_place_image(place, place_image_url, image_filename):
    response = requests.get(place_image_url)
    response.raise_for_status()

    place_image = PlaceImage(place=place)
    place_image.image.save(image_filename, ContentFile(response.content))


class Command(BaseCommand):
    help = 'Load place from json file'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            required=True
        )

    def handle(self, *args, **options):
        file_path = options['path']

        if not os.path.exists(file_path):
            raise CommandError(f'{file_path} - file path does not exist')

        with open(file_path) as json_file:
            place = json.load(json_file)

        place_entry = Place.objects.create(
            title=place['title'],
            description_short=place['description_short'],
            description_long=place['description_long'],
            coordinate_lng=place['coordinates']['lng'],
            coordinate_lat=place['coordinates']['lat']
        )

        for num, image_url in enumerate(place['imgs'], start=1):
            image_filename = f'{num}_{place["title"]}.jpg'
            create_place_image(place_entry, image_url, image_filename)
