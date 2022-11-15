from django.urls import path
from . import views

app_name = "app_upload"

urlpatterns = [
    path("", views.upload_image, name="image_upload"),
]
