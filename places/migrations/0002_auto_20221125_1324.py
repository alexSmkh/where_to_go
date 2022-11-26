# Generated by Django 3.0 on 2022-11-25 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinate_lat',
            field=models.FloatField(help_text='Координаты(широта)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinate_lng',
            field=models.FloatField(help_text='Координаты(долгота)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.DateTimeField(help_text='Дата создания'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=models.CharField(help_text='Полное описание', max_length=10000),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(help_text='Короткое описание', max_length=1000),
        ),
        migrations.AlterField(
            model_name='place',
            name='published_at',
            field=models.DateTimeField(blank=True, help_text='Дата публикации', null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(help_text='Название', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_at',
            field=models.DateTimeField(blank=True, help_text='Дата обновления', null=True),
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='place_images')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='image', to='places.Place')),
            ],
        ),
    ]