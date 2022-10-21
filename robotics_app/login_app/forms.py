from django.forms import ModelForm, TextInput
from django import forms 
from .models import Users

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username':TextInput(attrs={'placeholder': 'Username'}),
            'password': TextInput(attrs={'placeholder': 'Password'}),
        }
    