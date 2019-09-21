from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    short_url = models.SlugField(max_length=200, unique=True)
    url = models.URLField(max_length=200)
    date_submited = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return self.url

