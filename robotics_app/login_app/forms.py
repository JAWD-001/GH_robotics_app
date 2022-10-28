from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users, Summaries
from django.contrib.auth.password_validation import validate_password

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['USERNAME_FIELD', 'password1']
        widgets = {
            'USERNAME_FIELD':TextInput(attrs={'placeholder': 'Username'}),
            'password1':PasswordInput(attrs={'placeholder': 'Password'}),
        }
        
class CreateUserForm(UserCreationForm):
    confirm_email = forms.CharField(widget=TextInput(attrs={'placeholder':'Confirm Email'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = Users
        fields = ['first_name','last_name','USERNAME_FIELD','password1','password2','email', 'confirm_email']
        widgets = {
            'first_name':TextInput(attrs={'placeholder': 'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
            'USERNAME_FIELD':TextInput(attrs={'placeholder':'Username'}),
            'email':TextInput(attrs={'placeholder':'Email'}),
        }

          
class SummaryNotesForm(ModelForm):
    class Meta:
        model=Summaries
        fields = '__all__'
        widgets ={}
    