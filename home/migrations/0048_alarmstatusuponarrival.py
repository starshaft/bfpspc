# Generated by Django 3.0.8 on 2020-12-28 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20201229_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmStatusUponArrival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StatusUponArrival', models.CharField(blank=True, choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd')], default='closed', max_length=255)),
                ('StatusUponArrivalRemarks', models.CharField(blank=True, max_length=255)),
                ('Incident', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Incident')),
            ],
        ),
    ]
