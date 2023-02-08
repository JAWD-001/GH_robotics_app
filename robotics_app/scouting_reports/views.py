from django.views.generic import TemplateView, DetailView, CreateView, ListView
from .models import ScoutingReport

from .forms import ScoutingReportForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

class ScoutingOptionsView(LoginRequiredMixin, TemplateView):
    template_name = 'scouting_reports/scouting.html'

class ScoutingReportsView(LoginRequiredMixin, ListView):
    model = ScoutingReport
    template_name = 'scouting_reports/scouting_reports_list.html'
    context_object_name = 'scouting_reports'
    paginate_by = 2

class ScoutingReportCreateView(LoginRequiredMixin,CreateView):
    form_class = ScoutingReportForm
    success_url = reverse_lazy('scouting:scouting_reports')
    template_name = 'scouting_reports/scouting_reports_form.html'

class ScoutingReportDetailView(LoginRequiredMixin,DetailView):
    model = ScoutingReport
    context_object_name = 'scouting_reports'
    template_name = 'scouting_reports/scouting_reports_detail.html'
