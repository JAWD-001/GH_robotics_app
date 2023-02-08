from django.forms import ModelForm, DateField

from django import forms
from django.forms import widgets

from .models import ScoutingReport, OpposingTeam

class ScoutingReportForm(forms.ModelForm):
    class Meta:
        model = ScoutingReport
        fields = '__all__'
        widgets = {'date': widgets.SelectDateWidget()
        }