from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app1.urls")),  # Здесь include на app1/urls.py
]
