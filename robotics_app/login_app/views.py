from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from login_app.forms import LoginForm, CreateUserForm, CustomPasswordResetForm
from login_app.models import Users
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView
# Create your views here.

class LoginFormView(LoginView):
    authentication_form = LoginForm
    form_class = LoginForm
    template_name = 'login_app/login.html'
    redirect_authenticated_user = True
    success_url = 'login'
    
    
class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'login_app/create_user.html'
    success_url = reverse_lazy('login:login.html')
    
class PasswordResetView(FormView):
    form_class = CustomPasswordResetForm
    template_name = 'login_app/password_reset_form.html'
    success_url = reverse_lazy('login:login.html')