from django.urls import path

from pages.views import DashboardPageView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
]
