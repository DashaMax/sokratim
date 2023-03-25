from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class User(AbstractUser):
    slug = models.SlugField(verbose_name='URL', max_length=160, unique=True)
    email = models.EmailField(verbose_name='Email', max_length=128, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})
