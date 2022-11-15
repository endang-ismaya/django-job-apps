from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Subscribe
from .forms import SubscribeForm


def thank_you(request):
    context = {}
    return render(
        request=request, template_name="app_subscribe/thankyou.html", context=context
    )


def subscribe(request):
    email_error_empty = ""
    subscribe_form = SubscribeForm()

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)

        if subscribe_form.is_valid():
            # email = subscribe_form.cleaned_data["email"]
            # first_name = subscribe_form.cleaned_data["first_name"]
            # last_name = subscribe_form.cleaned_data["last_name"]

            # subscribe_new = Subscribe(
            #     first_name=first_name, last_name=last_name, email=email
            # )
            # subscribe_new.save()
            subscribe_form.save()
            return redirect(reverse("app_subscribe:thank_you"))

    context = {
        "form": subscribe_form,
        "email_error_empty": email_error_empty,
    }
    return render(request, "app_subscribe/email.html", context)
