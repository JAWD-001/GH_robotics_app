from django.forms import ModelForm, TextInput

from django import forms
from .models import BuildSummary

'''class BuildSummaryForm(forms.ModelForm):
    build_summary_image = ImageField(widgets = forms.ImageField(attrs={class}))
    class Meta:
        model = BuildSummary
        fields = ['subteam', 'summary_date', 'daily_goal', 'work_accomplished', 'challenges_faced', 'tomorrow_goal', 'build_summary_image,']
        widgets = {'performance_description': forms.DateInput
        
        forms.(attrs={})
            'text': forms.
        }
'''