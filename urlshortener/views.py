from django.shortcuts import render
from .forms import UrlshortenerForm


def shortener(request):

    if request.method == 'POST':
        form = UrlshortenerForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UrlshortenerForm()

    return render(request, 'urlshortener/shortener.html', {'form': form})
