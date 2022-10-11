from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from login_app.forms import LoginForm
from login_app.models import Users
from django.urls import reverse_lazy

# Create your views here.

class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login_app/login.html'
    
class UserCreateView(CreateView):
    model = Users
    template_name = 'login_app/user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('login_app:login.html')
    