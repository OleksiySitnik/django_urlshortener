from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form': form})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile,
        'profile_page': 'active'
    }

    return render(request, 'users/profile.html', context)

