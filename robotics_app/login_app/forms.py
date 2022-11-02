from django.forms import ModelForm, TextInput, PasswordInput, EmailField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django import forms
from .models import Users, Summaries
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import get_user_model

Users = get_user_model()

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'username':TextInput(attrs={'placeholder': 'Username'}),
            'password':PasswordInput(attrs={'placeholder': 'Password'}),
        }
        
class CreateUserForm(UserCreationForm):
    confirm_email = forms.EmailField(widget=TextInput(attrs={'placeholder':'Confirm Email'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ['first_name','last_name','username', 'password','email', 'confirm_email']
        widgets = {
            'first_name':TextInput(attrs={'placeholder': 'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
            'username':TextInput(attrs={'placeholder':'Username'}),
            'email':TextInput(attrs={'placeholder':'Email'}),
            'password':PasswordInput(attrs={'placeholder':'Password from model'}),
        }
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = '__all__'
          
class SummaryNotesForm(ModelForm):
    class Meta:
        model=Summaries
        fields = '__all__'
        widgets ={}
        
class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = Users
        fields = ['email']
        widgets = {
            'email':TextInput(attrs={'placeholder':'Email'}),
        }
    