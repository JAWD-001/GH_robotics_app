# Generated by Django 4.1.3 on 2023-01-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouting_reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoutingreport',
            name='scoring_cap_placed',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2),
        ),
        migrations.AddField(
            model_name='scoutingreport',
            name='scoring_cap_placement',
            field=models.CharField(blank=True, choices=[('Floor', 'Floor'), ('Low', 'Low Level'), ('Medium', 'Medium Level'), ('High', 'High Level')], max_length=10),
        ),
    ]
