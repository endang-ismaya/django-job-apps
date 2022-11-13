from django.urls import path
from . import views

app_name = "app_one"

urlpatterns = [
    path("", views.job_list, name="jobs_home"),
    path("job/<int:id>", views.job_detail, name="jobs_detail"),
]
