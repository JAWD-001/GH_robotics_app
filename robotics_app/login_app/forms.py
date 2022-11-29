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
    use_required_attribute = False
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password - Min of 9 alphanumeric characters and 1 special character'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ['first_name','last_name','username','email','grad_year']
        error_messages = {
            'first_name':{'required': 'First name cannot be blank or null', 'min_length': 'First name must be at least 2 characters long'},
            'last_name':{'required': 'Last name cannot be blank or null','min_length': 'Last name must be at least 2 characters long'},
            'username':{'required': 'Username cannot be blank or null', 'min_length': 'Username must be at least 2 characters long'},
            'email':{'required': 'Email cannot be null or blank', 'required': 'Grad Year cannot be blank or null'}}
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