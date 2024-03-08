from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")

        return super().dispatch(request, *args, **kwargs)


class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard.html"
