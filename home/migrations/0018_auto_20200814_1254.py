# Generated by Django 3.0.8 on 2020-08-14 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200814_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Cause',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='HouseNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Origin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
