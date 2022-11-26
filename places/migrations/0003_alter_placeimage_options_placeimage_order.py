# Generated by Django 4.1.3 on 2022-11-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20221125_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='placeimage',
            name='order',
            field=models.PositiveSmallIntegerField(db_index=True, default=0),
        ),
    ]