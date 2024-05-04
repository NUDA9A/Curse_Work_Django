from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    verification_code = models.CharField(max_length=20, verbose_name="Ключ верификации", **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name="Статус пользователя")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("set_active", "Can change is_active field"),
        ]
