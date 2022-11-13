from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import LoginForm, CreateUserForm, CustomPasswordResetForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from login_app.models import Users
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'login_app/create_user.html'
    success_url = reverse_lazy('login:home')


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

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'login_app/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('login:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
        template_name = "login_app/password_reset_complete.html"

    