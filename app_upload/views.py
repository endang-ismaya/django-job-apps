from django.shortcuts import render
from .forms import UploadForm, UploadFileForm


def upload_image(request):

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            saved_obj = form.instance
            context = {"form": form, "saved_obj": saved_obj}
            return render(request, "app_upload/add_image.html", context)
    else:
        form = UploadForm()

    context = {"form": form}
    return render(request, "app_upload/add_image.html", context)


def upload_file(request):

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            saved_obj = form.instance
            context = {"form": form, "saved_obj": saved_obj}
            return render(request, "app_upload/add_file.html", context)
    else:
        form = UploadFileForm()

    context = {"form": form}
    return render(request, "app_upload/add_file.html", context)
