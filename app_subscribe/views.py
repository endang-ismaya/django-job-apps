from django.shortcuts import render
from .models import Subscribe
from .forms import SubscribeForm

# Create your views here.
def subscribe(request):
    email_error_empty = ""
    subscribe_form = SubscribeForm()

    if request.POST:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        if email == "":
            email_error_empty = "No email entered"

        subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
        subscribe.save()

    context = {
        "form": subscribe_form,
        "email_error_empty": email_error_empty,
    }
    return render(request, "app_subscribe/subscribe.html", context)
