# Generated by Django 3.0.8 on 2020-08-05 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_incident_totalfatalities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='FireArsonInvestigator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Investigator'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Remarks',
            field=models.CharField(blank=True, choices=[('closed', 'Closed'), ('under investigation', 'Under Investigation'), ('', '')], default='closed', max_length=255),
        ),
    ]
