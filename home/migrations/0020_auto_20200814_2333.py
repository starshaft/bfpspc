# Generated by Django 3.0.8 on 2020-08-14 15:33

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200814_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barangay',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='barangay',
            name='Longitude',
        ),
        migrations.AddField(
            model_name='barangay',
            name='Location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
