from django.db import models

SUBTEAMS = (
        ('')

)

class Teams(models.Model):
        class SubTeamNames(models.TextChoices):
                CODING = 'CD'
                ENGINEERING = 'EG'
                DRIVETRAIN = 'DT'
                SPIRIT = 'SP'

        id = models.BigAutoField(primary_key=True)
        subteam = models.CharField(max_length=2, choices=SubTeamNames.choices, default=SubTeamNames.ENGINEERING)



# Create your models here.
