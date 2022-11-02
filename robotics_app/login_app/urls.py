from django.urls import path
from .views import LoginFormView, CreateUserView, ForgotPasswordView

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(), name='login'),
    path('create', CreateUserView.as_view(), name='create'),
    path('forgot_password', ForgotPasswordView.as_view(), name='forgot_password')
]