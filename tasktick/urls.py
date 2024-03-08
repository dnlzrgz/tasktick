"""
URL configuration for tasktick project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from tasktick.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("pages.urls")),
    path("api/v1/", api.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
