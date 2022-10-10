from django.urls import path
from .views import LoginFormView

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(), name='login'),
]