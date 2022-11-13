from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound

jobs = [
    ("First Job", "This is the First Job"),
    ("Second Job", "This is the Second Job"),
    ("Third Job", "This is the Third Job"),
    ("Fourth Job", "This is the Fourth Job"),
    ("Fifth Job", "This is the Fifth Job"),
]


def job_list(request):
    templ = "<ul>"
    for index, j in enumerate(jobs):
        job_detail_url = reverse("app_one:jobs_detail", args=(index,))
        templ += f"<li><a href='{job_detail_url}'>{j[0]}</a></li>"

    templ += "</ul>"
    return HttpResponse(templ)


def job_detail(request, id):

    try:

        if id >= len(jobs):
            return redirect(reverse("app_one:jobs_home"))

        job_title = jobs[id][0]
        job_desc = jobs[id][1]

        templ = f"<h1>{job_title}</h1>"
        templ += f"<h3>{job_desc}</h3>"
        return HttpResponse(templ)

    except:

        return HttpResponseNotFound("Job Not Found!.")
