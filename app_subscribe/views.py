from django.shortcuts import render
from .models import Subscribe
from .forms import SubscribeForm

# Create your views here.
def subscribe(request):
    email_error_empty = ""
    subscribe_form = SubscribeForm()

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)

        if subscribe_form.is_valid():
            print("Form is Valid")

        # if email == "":
        #     email_error_empty = "No email entered"

        # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
        # subscribe.save()

    context = {
        "form": subscribe_form,
        "email_error_empty": email_error_empty,
    }
    return render(request, "app_subscribe/subscribe.html", context)
