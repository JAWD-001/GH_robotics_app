from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# Create your views here.

class LoginView(TemplateView):
    template_name = 'login_app/login.html'