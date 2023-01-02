from django.db import models

# Create your models here.
class OpposingTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_number = models.IntegerField(blank=True, unique=True)
    team_name = models.CharField(blank=True, max_length=200, unique=True)
    team_school = models.CharField(blank=True, max_length=200)
    team_contact = models.CharField(blank=True, max_length=200)


class ScoutingReport(models.Model):
    id = models.BigAutoField(primary_key=True)