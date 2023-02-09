from django.forms import ModelForm, TextInput
from django import forms
from django.forms import widgets

from .models import BuildSummary

class BuildSummaryForm(forms.ModelForm):
    class Meta:
        model = BuildSummary
        fields = ['subteam', 'summary_date', 'daily_goal', 'work_accomplished', 'challenges_faced', 'tomorrow_goal', 'build_summary_image']
        widgets = {'summary_date': widgets.NumberInput(attrs={'type': 'date'})}
