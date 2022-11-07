from django.forms import ModelForm, TextInput, PasswordInput, EmailField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, AuthenticationForm
from django import forms
from .models import Users, Summaries
from django.contrib.auth.password_validation import validate_password

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
    confirm_email = forms.EmailField(widget=TextInput(attrs={'placeholder':'Confirm Email'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password - must be at least 9 alphanumeric characters'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
       model = Users
       fields = ['first_name','last_name','username','email', 'confirm_email']
       widgets = {
            'first_name':TextInput(attrs={'placeholder': 'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
            'username':TextInput(attrs={'placeholder':'Username'}),
            'email':TextInput(attrs={'placeholder':'Email'}),
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
    
    
class SummaryNotesForm(ModelForm):
    class Meta:
        model=Summaries
        fields = '__all__'
        widgets ={}