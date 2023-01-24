from django.db import models
from datetime import date

class BuildSummary(models.Model):
        class SubTeamNames(models.TextChoices):
                CODING = 'CD'
                ENGINEERING = 'EG'
                DRIVETRAIN = 'DT'
                SPIRIT = 'SP'

        id = models.BigAutoField(primary_key=True)
        subteam = models.CharField(max_length=2, choices=SubTeamNames.choices, default=SubTeamNames.ENGINEERING)
        summary_date = models.DateField(default=date.today)
        daily_goal = models.TextField(blank=True)
        work_accomplished = models.TextField(blank=True)
        challenges_faced = models.TextField(blank=True)
        tomorrow_goal = models.TextField(max_length=100, blank=True)
        build_summary_image = models.ImageField(blank=True, upload_to="build_images")


        def __str__(self):
                return self.subteam, self.summary_date, self.daily_goal, self.work_accomplished, self.challenges_faced, self.tomorrow_goal, self.build_summary_image


# Create your models here.


