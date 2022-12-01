import glob
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


def create_place(filepath):
    with open(filepath) as json_file:
        place = json.load(json_file)

    place_entry = Place.objects.create(
        title=place['title'],
        description_short=place['description_short'],
        description_long=place['description_long'],
        longitude=place['coordinates']['lng'],
        latitude=place['coordinates']['lat']
    )

    for num, image_url in enumerate(place['imgs'], start=1):
        image_filename = f'{num}_{place["title"]}.jpg'
        create_place_image(place_entry, image_url, image_filename)


class Command(BaseCommand):
    help = 'Load place from json file'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            required=True
        )

    def handle(self, *args, **options):
        path = options['path']

        if not os.path.exists(path):
            raise CommandError(f'{path} - path does not exist')

        if os.path.isfile(path):
            create_place(path)
            return

        filepaths = [filepath for filepath in glob.glob(os.path.join(path, '*.json'))]

        for filepath in filepaths:
            create_place(filepath)
