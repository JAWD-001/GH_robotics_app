from django.views.generic import TemplateView, FormView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import BuildSummary
# Create your views here.

#CLASS BASED VIEW FOR BUILD OPTIONS HOMEPAGE
class BuildOptionsView(LoginRequiredMixin, TemplateView):
    template_name = 'build_summaries/build_options.html'


#CLASS BASED VIEW FOR BUILD SUMMARIES LIST VIEW
class BuildSummariesView(LoginRequiredMixin, ListView):
    model = BuildSummary
    template_name = 'build_summaries/build_summary_list.html'

class BuildSummariesCreateView(LoginRequiredMixin, CreateView):
    model = BuildSummary
    fields = "__all__"
    success_url = reverse_lazy('builds:build_summaries_list')
    template_name = 'build_summaries/build_summaries_form.html'