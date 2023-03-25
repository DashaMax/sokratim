from django.db import models

from users.models import User


class Link(models.Model):
    username = models.ForeignKey(to=User, on_delete=models.CASCADE)
    long_link = models.URLField(verbose_name='Длинная ссылка', max_length=250)
    short_link = models.CharField(verbose_name='Сокращённая ссылка', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.short_link

