from django.db import models

class Teams(models.Model):
        class SubTeamNames(models.TextChoices):
                CODING = 'CD'
                ENGINEERING = 'EG'
                DRIVETRAIN = 'DT'
                SPIRIT = 'SP'

        id = models.BigAutoField(primary_key=True)
        subteam = models.CharField(max_length=2, choices=SubTeamNames.choices, default=SubTeamNames.ENGINEERING)
        daily_goal = models.TextField(blank=True, Null=True)
        work_accomplished = models.TextField(blank=True, Null=True)
        challenges_faced = models.TextField(blank=True, Null=True)
        tomorrow_goal = models.CharField(max_length=500, blank=True, Null=True)
        build_summary_image = models.ImageField(blank=True, null=True, upload_to="build_images")



# Create your models here.
