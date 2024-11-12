from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, ManyToManyField, EmailField, Model


class CustomUser(AbstractUser):
    username = None
    name = CharField(max_length=255, null=True, blank=True)
    USERNAME_FIELD = 'email'
    email = EmailField(unique=True)
    phone_number = CharField(max_length=30, null=True, blank=True)
    favorite = ManyToManyField("shop.Product", blank=True)
    REQUIRED_FIELDS = []
