from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    short_url = models.SlugField(max_length=200)
    url = models.URLField(max_length=200)
    date_submited = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):

