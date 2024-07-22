from django.db import models

class Subscriber(models.Model):
    email = models.EmailField('Электронная почта', unique=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self) -> str:
        return self.email