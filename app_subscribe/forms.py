from django import forms


class SubscribeForm(forms.Form):
    first_name = forms.CharField(
        max_length=100, label="Enter first name", help_text="Enter character only"
    )
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    username = forms.CharField(disabled=True)
