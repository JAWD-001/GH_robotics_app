from django.urls import path

from .views import ScoutingOptionsView, ScoutingReportsView

app_name = 'scouting'

urlpatterns = [
#URL ROUTING FOR SCOUTING OPTIONS HOME
    path('scouting_options/', ScoutingOptionsView.as_view(), name='scouting_options'),

#URL ROUTING FOR SCOUTING REPORTS FORM
    path('scouting_reports/', ScoutingReportsView.as_view(), name='scouting_reports'),

]