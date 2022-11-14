from django import forms
from .models import Subscribe
from django.utils.translation import gettext_lazy as _

# def validate_comma(value):
#     if "," in value or len(value) < 5:
#         raise forms.ValidationError("Invalid Lastname")
#     return value

# ModelForm
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        # exclude = ("first_name",)
        # fields = ["first_name", "last_name", "email"]
        fields = "__all__"
        labels = {
            "first_name": _("Firstname"),
            "last_name": _("Lastname"),
            "email": _("Email"),
        }
        help_texts = {"first_name": _("Chars only no more than 100 chars")}
        error_messages = {
            "first_name": {
                "required": _("Please enter a valid 'Firstname' no more than 100 chars")
            }
        }

    def clean_first_name(self):
        data = self.cleaned_data.get("first_name", None)
        if data is None:
            raise forms.ValidationError("First Name Not Found")
        elif "," in data or len(data) < 5:
            raise forms.ValidationError("Invalid Firstname")
        return data

    def clean_last_name(self):
        data = self.cleaned_data.get("last_name", None)
        if data is None:
            raise forms.ValidationError("Lastname Not Found")
        elif "," in data or len(data) < 5:
            raise forms.ValidationError("Invalid Lastname")
        return data


# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=100, label="Firstname", help_text="Enter character only"
#     )
#     last_name = forms.CharField(
#         max_length=100, validators=[validate_comma], label="Lastname"
#     )
#     email = forms.EmailField(max_length=100, label="Email")
#     # username = forms.CharField(disabled=True)

#     # Validation
#     def clean_first_name(self):
#         data = self.cleaned_data["first_name"]
#         if "," in data or len(data) < 5:
#             raise forms.ValidationError("Invalid First Name")
#         return data
