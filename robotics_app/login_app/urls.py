from django.urls import path
from .views import LoginFormView, CreateUserView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView, ForgotUsernameView, ForgotUsernameDoneView, UserHomeView, ScoutingOptionsView, BuildOptionsView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'login'

urlpatterns =[
    path('', LoginFormView.as_view(authentication_form=LoginForm), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', CreateUserView.as_view(), name='create'),

    path('reset_password_form/', CustomPasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name='login_app/password_reset_confirm.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login_app/password_reset_complete.html'), name ='password_reset_complete'),

    path('forgot_username/', ForgotUsernameView.as_view(), name='forgot_username'),
    path('forgot_username_done/', ForgotUsernameDoneView.as_view(template_name='login_app/forgot_username_done.html'), name='forgot_username_done'),

    path('home/', UserHomeView.as_view(), name='user_home'),
    path('scouting_options', ScoutingOptionsView.as_view(), name='scouting_options'),
    path('build_options', BuildOptionsView.as_view(), name='build_options')
]