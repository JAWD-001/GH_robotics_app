from django.urls import path
from .views import BuildOptionsView, BuildSummariesView, BuildSummariesCreateView, BuildSummaryDetailView

app_name = 'builds'

urlpatterns = [\
    #URL ROUTING FOR BUILD OPTIONS HOME
    path('build_options/', BuildOptionsView.as_view(), name='build_options'),

    #URL ROUTING FOR LISTVIEW OF BUILD SUMMARIES
    path('build_summaries/', BuildSummariesView.as_view(), name='build_summaries'),

    #URL ROUTING FOR CREATEVIEW OF BUILD SUMMARIES
    path('build_summary_form/', BuildSummariesCreateView.as_view(), name='build_summaries_form'),

    #URL ROUTING FOR BUILD SUMMARY DETAILVIEW
    path('summary_detail/<int:pk>', BuildSummaryDetailView.as_view(), name='summary_detail'),
]