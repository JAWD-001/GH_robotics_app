from django.urls import path

from .views import ScoutingOptionsView, ScoutingReportsView, ScoutingReportCreateView

app_name = 'scouting'

urlpatterns = [
#URL ROUTING FOR SCOUTING OPTIONS HOME
    path('scouting_options/', ScoutingOptionsView.as_view(), name='scouting_options'),

#URL ROUTING FOR SCOUTING REPORTS LIST
    path('scouting_reports/', ScoutingReportsView.as_view(), name='scouting_reports'),

#URL ROUTING FOR SCOUTING REPORT FORM
    path('scouting_report_form/', ScoutingReportCreateView.as_view(), name='scouting_report_form'),

]