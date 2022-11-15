from django.urls import path
from . import views

app_name = "app_one"

urlpatterns = [
    path("", views.job_list, name="jobs_home"),
    path("jobs/<slug:slug>", views.job_detail, name="jobs_detail"),
]
