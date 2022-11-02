from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from login_app.forms import LoginForm, CreateUserForm, ForgotPasswordForm
from login_app.models import Users
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login_app/login.html'
    
class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'login_app/create_user.html'
    success_url = reverse_lazy('login_app:login.html')
    
class ForgotPasswordView(FormView):
    form_class = ForgotPasswordForm
    template_name = 'login_app/forgot_password.html'
    success_url = reverse_lazy('login_app:login.html')