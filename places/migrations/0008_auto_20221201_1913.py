# Generated by Django 4.1.3 on 2022-12-01 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_coordinate_lat_and_more'),
    ]

    operations = [
        migrations.RenameField('Place', 'coordinate_lng', 'longitude'),
        migrations.RenameField('Place', 'coordinate_lat', 'latitude')
    ]
