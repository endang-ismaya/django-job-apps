from django.urls import path
from . import views

app_name = "app_subscribe"

urlpatterns = [
    path("", views.subscribe, name="subscribe"),
]
