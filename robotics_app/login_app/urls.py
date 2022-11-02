from django.urls import path
from .views import LoginFormView, CreateUserView, PasswordResetView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(authentication_form=LoginForm), name='home'),
    path('create', CreateUserView.as_view(), name='create'),
    path('password_reset', PasswordResetView.as_view(), name='password_reset')
]