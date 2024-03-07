"""
URL configuration for tasktick project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from tasktick.api import api

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home",
    ),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/v1/", api.urls),
]
