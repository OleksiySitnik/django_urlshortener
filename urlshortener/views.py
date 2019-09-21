from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect


from .forms import UrlshortenerForm
from .utils import generate_key
from users.models import Profile
from .models import Url


def shortener_page(request):
    form = UrlshortenerForm()
    return render(request, 'urlshortener/shortener.html', {'form': form, 'shortener_page': 'active'})

def shortener_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = UrlshortenerForm(request.POST)

        if form.is_valid():
            obj = Url.objects.filter(url=request.POST['url'])

            if obj.exists():
                return JsonResponse({'short_url': obj[0].short_url})

            url = form.save(commit=False)
            short_url = url.short_url = generate_key()
            url.save()

            if current_user.is_authenticated:
                profile = Profile.objects.get(user=current_user)
                profile.urls.add(url)

            return JsonResponse({'short_url': short_url})

def shortener_redirect(request, short_url):
    url = Url.objects.get(short_url=short_url)
    return redirect(url)