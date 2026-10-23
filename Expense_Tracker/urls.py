from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def dashboard(request):
    return render(request, "tracker/dashboard.html")


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("admin/", admin.site.urls),
    path("api/account/", include("accounts.urls")),
    path("api/categories/", include("categories.urls")),
    path("api/transactions/", include("transactions.urls")),
]