from django.db import models
from datetime import date
# Create your models here.


class OpposingTeam(models.Model):
    class Meta:
        ordering = ['team_number']

    id = models.BigAutoField(primary_key=True)
    team_number = models.IntegerField(blank=True, unique=True)
    team_name = models.CharField(blank=True, max_length=200, unique=True)
    team_school = models.CharField(blank=True, max_length=200)
    team_contact = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.team_name

class ScoutingReport(models.Model):
    class Option(models.TextChoices):
        YES = 'Y'
        NO = 'N'

    class ConePlacementLocations(models.TextChoices):
        STATION = 'Station'
        JUNCTIONS = 'Junction'
        POLE = 'Pole'
        HIGH_POLE = 'High Pole'

    class StackLevels(models.TextChoices):
        FLOOR = 'Floor'
        LOW_LEVEL = 'Low'
        MEDIUM_LEVEL = 'Medium'
        HIGH_LEVEL = 'High'

    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=date.today)
    team = models.ForeignKey(OpposingTeam, to_field='team_name', on_delete=models.CASCADE)
    autonomous_scoring = models.CharField(blank=True, max_length=2, choices=Option.choices, default=Option.NO)
    autonomous_cone_placement = models.CharField(blank=True, max_length=12, choices=ConePlacementLocations.choices)
    parked_autonomously = models.CharField(blank=True, max_length=2, choices=Option.choices, default=Option.NO)
    clear_out_wait_time = models.CharField(blank=True, max_length=2, choices=Option.choices, default=Option.NO)
    side_cone_stacks = models.CharField(blank=True, max_length=2, choices=Option.choices, default=Option.NO)
    cone_stacks_level = models.CharField(blank=True, max_length=10, choices=StackLevels.choices)
    circuit_completed = models.CharField(blank=True, max_length=2, choices=Option.choices, default=Option.NO)
    scoring_cap_placed = models.CharField(blank=True, max_length=2, choices=Option.choices, default=Option.NO)
    scoring_cap_placement = models.CharField(blank=True, max_length=10, choices=StackLevels.choices)
    performance_description = models.TextField(blank=True)
    
