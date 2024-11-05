from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, ManyToManyField


class CustomUser(AbstractUser):
    phone_number = CharField(max_length=30, null=True, blank=True)
    favorite = ManyToManyField("shop.Product", blank=True)
