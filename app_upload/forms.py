from django import forms
from .models import Upload, UploadFile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = "__all__"


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = "__all__"
