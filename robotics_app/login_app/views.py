from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from login_app.forms import LoginForm

# Create your views here.

class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login_app/login.html'