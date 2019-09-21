"""django_urlshortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from urlshortener import views as urlsh_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('', urlsh_views.shortener_page, name='shortener'),
    path('short/', urlsh_views.shortener_post, name='ajax_shortener'),
    re_path('(?P<short_url>[a-zA-Z0-9_-]+)/', urlsh_views.shortener_redirect, name='shortener_redirect' )
    # path('',urlsh_views.URLShortenerView.as_view(), name='shortener')
]
