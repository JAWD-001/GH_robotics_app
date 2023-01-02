from django.urls import path
from .views import BuildOptionsView, BuildSummariesView

app_name = 'builds'

urlpatterns = [\
    #URL ROUTING FOR BUILD OPTIONS HOME
    path('build_options/', BuildOptionsView.as_view(), name='build_options'),

    #URL ROUTING FOR LISTVIEW OF BUILDSUMMARIES
    path('build_summaries/', BuildSummariesView.as_view(), name='build_summaries'),


]