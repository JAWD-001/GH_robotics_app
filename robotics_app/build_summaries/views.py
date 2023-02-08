from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import BuildSummary
from .forms import BuildSummaryForm
# Create your views here.

#CLASS BASED VIEW FOR BUILD OPTIONS HOMEPAGE
class BuildOptionsView(LoginRequiredMixin, TemplateView):
    template_name = 'build_summaries/build_options.html'


#CLASS BASED VIEW FOR BUILD SUMMARIES LIST VIEW
class BuildSummariesView(LoginRequiredMixin, ListView):
    model = BuildSummary
    template_name = 'build_summaries/build_summary_list.html'
    context_object_name = 'build_summaries'
    paginate_by = 4

class BuildSummariesCreateView(LoginRequiredMixin, CreateView):
    form_class = BuildSummaryForm
    success_url = reverse_lazy('builds:build_summaries')
    template_name = 'build_summaries/build_summaries_form.html'

class BuildSummaryDetailView(LoginRequiredMixin, DetailView):
    model = BuildSummary
    context_object_name = 'build_summaries'
    template_name = 'build_summaries/build_summary_detail.html'