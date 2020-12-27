# Generated by Django 3.0.8 on 2020-12-27 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='ChiefOfficer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officer_bfp', to='home.Personnel'),
        ),
    ]
