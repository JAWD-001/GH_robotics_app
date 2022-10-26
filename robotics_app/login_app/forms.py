from django.forms import ModelForm, TextInput
from django import forms 
from .models import Users, Summaries

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username':TextInput(attrs={'placeholder': 'Username'}),
            'password':TextInput(attrs={'placeholder': 'Password'}),
        }
        
class CreateUserForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        widgets = {
            'first_name':TextInput(attrs={'placeholder': 'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
            'username':TextInput(attrs={'placeholder':'Username'}),
            'password':TextInput(attrs={'placeholder':'Password'}),
            'email':TextInput(attrs={'placeholder':'Email'}),
        }

class SummaryNotesForm(ModelForm):
    class Meta:
        model=Summaries
        fields = '__all__'
        widgets ={}
    