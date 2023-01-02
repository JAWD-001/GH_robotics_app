from django.urls import path
from .views import LoginFormView, CreateUserView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView, ForgotUsernameView, ForgotUsernameDoneView, UserHomeView, ScoutingOptionsView, BuildOptionsView, \
    ScoutingReportsView, BuildSummariesView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'login'

urlpatterns = [
#LOGIN, LOGOUT, AND ACCOUNT CREATION URL ROUTING
    path('', LoginFormView.as_view(authentication_form=LoginForm), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', CreateUserView.as_view(), name='create'),

#PASSWORD RESET/RECOVERY URL ROUTING
    path('reset_password_form/', CustomPasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name='login_app/password_reset_confirm.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login_app/password_reset_complete.html'), name ='password_reset_complete'),

#FORGOT USERNAME RECOVERY URL ROUTES
    path('forgot_username/', ForgotUsernameView.as_view(), name='forgot_username'),
    path('forgot_username_done/', ForgotUsernameDoneView.as_view(template_name='login_app/forgot_username_done.html'), name='forgot_username_done'),

#URL ROUTING FOR SCOUTING AND BUILD REPORTS
    path('home/', UserHomeView.as_view(), name='user_home'),
    path('scouting_options/', ScoutingOptionsView.as_view(), name='scouting_options'),
    path('build_options/', BuildOptionsView.as_view(), name='build_options'),

#URL ROUTING FOR SCOUTING AND BUILDING LIST VIEWS
    path('scouting_reports/', ScoutingReportsView.as_view(), name='scouting_reports'),
    path('build_summaries/', BuildSummariesView.as_view(), name='build_summaries'),
]