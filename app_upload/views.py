from django.shortcuts import render
from .forms import UploadForm


def upload_image(request):
    form = UploadForm()
    context = {"form": form}
    return render(request, "app_upload/add_image.html", context)
