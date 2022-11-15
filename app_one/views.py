from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from .models import JobPost


def job_list(request):
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app_one/index.html", context)


def job_detail(request, slug):

    try:

        job = JobPost.objects.get(slug=slug)
        context = {"job": job}
        return render(
            request,
            "app_one/job_detail.html",
            context,
        )

    except:

        return HttpResponseNotFound("Job Not Found!.")
