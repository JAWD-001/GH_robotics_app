# Generated by Django 4.1.3 on 2023-01-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouting_reports', '0003_alter_opposingteam_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoutingreport',
            name='performance_description',
            field=models.TextField(blank=True),
        ),
    ]
