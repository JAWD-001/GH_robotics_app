from django.forms import ModelForm, TextInput, PasswordInput, EmailField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, AuthenticationForm
from django import forms
from .models import Users, Summaries
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

Users = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = AuthenticationForm
        AuthenticationFormFields = ('username', 'password')
        exclude = []
        
        
class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password - Min of 9 alphanumeric characters and 1 special character'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ['first_name','last_name','username','email', 'grad_year']
        widgets = {
            'first_name':TextInput(attrs={'placeholder': 'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
            'username':TextInput(attrs={'placeholder':'Username'}),
            'email':TextInput(attrs={'placeholder':'Email'}),
            'grad_year':TextInput(attrs={'placeholder':'Grad Year'}),
            'password':PasswordInput(attrs={'placeholder':'Password from model'}),
        }

        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Users
        fields = '__all__'
        
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=TextInput(attrs={'placeholder':'Email'}))
    class Meta:
        model = PasswordResetForm
        fields = ['email']
        widgets = {
            'email':TextInput(attrs={'placeholder':'Email'}),
        }


class ForgotUsernameForm(PasswordResetForm):
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = PasswordResetForm
        fields = ['email']
        widgets = {
            'email': TextInput(attrs={'placeholder': 'Email'}),
        }


class SummaryNotesForm(ModelForm):
    class Meta:
        model=Summaries
        fields = '__all__'
        widgets ={}