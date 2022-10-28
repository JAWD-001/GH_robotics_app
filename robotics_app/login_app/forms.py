from django.forms import ModelForm, TextInput
from django import forms 
from .models import Users, Summaries
from django.contrib.auth.password_validation import validate_password

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username':TextInput(attrs={'placeholder': 'Username'}),
            'password':TextInput(attrs={'placeholder': 'Password'}),
        }
        
class CreateUserForm(ModelForm):
    confirm_email = forms.CharField(widget=TextInput(attrs={'placeholder':'Confirm Email'}))
    confirm_password= forms.CharField(widget=TextInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = Users
        fields = ['first_name','last_name','username','password','confirm_password','email', 'confirm_email']
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
    