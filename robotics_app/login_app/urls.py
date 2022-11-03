from django.urls import path
from .views import LoginFormView, CreateUserView, CustomPasswordResetView, CustomPasswordResetDoneView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(authentication_form=LoginForm), name='home'),
    path('create', CreateUserView.as_view(), name='create'),
    path('reset_password/', CustomPasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]