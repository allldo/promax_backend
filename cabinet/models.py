from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, ManyToManyField, EmailField, Model
from django.utils.translation import gettext_lazy as _

from cabinet.managers import UserManager


class CustomUser(AbstractUser):
    username = None
    name = CharField(max_length=255, null=True, blank=True, verbose_name='имя')
    USERNAME_FIELD = 'email'
    email = EmailField(unique=True)
    phone_number = CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    favorite = ManyToManyField("shop.Product", blank=True, verbose_name='Избранные товары')
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"