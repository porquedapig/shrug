# Generated by Django 3.2.9 on 2022-06-05 00:06

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('menu_items', models.CharField(max_length=200)),
                ('reviews', models.IntegerField(default=0)),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
            ],
        ),
    ]
