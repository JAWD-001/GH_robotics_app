from django.forms import ModelForm
from .models import Users

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
    