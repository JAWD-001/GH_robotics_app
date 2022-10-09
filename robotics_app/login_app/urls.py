from django.urls import path
from .views import LoginView

app_name = 'login'

urlpatterns =[
    path('', LoginView.as_view(), name='login'),
]