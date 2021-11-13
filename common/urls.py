from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "common"

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="common:list_mail"), name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
