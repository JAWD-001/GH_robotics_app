from django.urls import path
from .views import LoginFormView, UserCreateView

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(), name='login'),
    path('create', UserCreateView.as_view(), name='create')
]