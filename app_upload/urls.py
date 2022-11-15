from django.urls import path
from . import views

app_name = "app_upload"

urlpatterns = [
    path("image/", views.upload_image, name="image_upload"),
    path("file/", views.upload_file, name="file_upload"),
]
