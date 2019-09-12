from django import forms
from .models import Url


class UrlshortenerForm(forms.ModelForm):
    url = forms.URLField()

    class Meta:
        model = Url
        fields = ['url']