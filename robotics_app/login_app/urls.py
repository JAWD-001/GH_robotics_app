from django.urls import path
from .views import LoginFormView, CreateUserView

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(), name='login'),
    path('create', CreateUserView.as_view(), name='create')
]