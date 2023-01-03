from django.views.generic import TemplateView, FormView, CreateView, ListView
from .models import ScoutingReport

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

class ScoutingOptionsView(LoginRequiredMixin, TemplateView):
    template_name = 'scouting_reports/scouting.html'

class ScoutingReportsView(LoginRequiredMixin, ListView):
    model = ScoutingReport
    template_name = 'scouting_reports/scouting_reports_list.html'

class ScoutingReportCreateView(LoginRequiredMixin,CreateView):
    model = ScoutingReport
    fields = '__all__'
    success_url = reverse_lazy('scouting:scouting_reports')
    template_name = 'scouting_reports/scouting_reports_form.html'
# Create your views here.
