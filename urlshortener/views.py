from django.shortcuts import render

from .forms import UrlshortenerForm
from .utils import generate_key
from users.models import Profile


def shortener(request):
    current_user = request.user

    if request.method == 'POST':
        form = UrlshortenerForm(request.POST)

        if form.is_valid():
            url = form.save(commit=False)
            url.short_url = generate_key()
            url.save()

            if current_user.is_authenticated:
                profile = Profile.objects.get(user=current_user)
                profile.urls.add(url)

    else:
        form = UrlshortenerForm()

    context = {
        'form': form,
        'shortener_page': 'active'
    }
    return render(request, 'urlshortener/shortener.html', context)
