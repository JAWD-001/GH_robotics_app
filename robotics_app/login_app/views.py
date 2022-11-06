from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from login_app.forms import LoginForm, CreateUserForm, CustomPasswordResetForm
from login_app.models import Users
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'login_app/create_user.html'
    success_url = reverse_lazy('login:login.html')


class LoginFormView(LoginView):
    form_class = LoginForm
    template_name = 'login_app/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login:password_reset')


class CustomPasswordResetView(PasswordResetView, SuccessMessageMixin):
    form_class = CustomPasswordResetForm
    email_template_name = 'login_app/password_reset_email.html'
    template_name = 'login_app/password_reset_form.html'
    success_url = reverse_lazy('login:password_reset_done')
    
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'login_app/password_reset_done.html'

    
    
    
    