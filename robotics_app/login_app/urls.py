from django.urls import path
from .views import LoginFormView, CreateUserView, PasswordResetView

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(), name='login'),
    path('create', CreateUserView.as_view(), name='create'),
    path('password_reset', PasswordResetView.as_view(), name='password_reset')
]