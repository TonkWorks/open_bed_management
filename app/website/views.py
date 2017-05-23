from django.conf import settings
from django.views import generic

from constance import config

from braces.views import LoginRequiredMixin


class HomePage(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"


class DashboardPage(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"