from django.views.generic import TemplateView, FormView, CreateView
from .forms import LoginForm, CreateUserForm, CustomPasswordResetForm, ForgotUsernameForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from login_app.models import Users
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'login_app/create_user.html'
    success_url = reverse_lazy('login:home')


class LoginFormView(LoginView):
    template_name = 'login_app/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('login:user_home')


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

class ForgotUsernameView(PasswordResetView, SuccessMessageMixin):
    form_class = ForgotUsernameForm
    email_template_name = 'login_app/forgot_username_email.html'
    template_name = 'login_app/forgot_username_form.html'
    success_url = reverse_lazy('login:forgot_username_done')

class ForgotUsernameDoneView(PasswordResetDoneView):
    template_name = 'login_app/forgot_username_done.html'


class UserHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'login_app/home.html'
    login_url = '/login/'
    redirect_field_name = 'login'

class ScoutingOptionsView(LoginRequiredMixin, TemplateView):
    template_name = 'login_app/scouting.html'

class BuildOptionsView(LoginRequiredMixin, TemplateView):
    template_name = 'login_app/build_options.html'
