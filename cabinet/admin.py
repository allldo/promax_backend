from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cabinet.models import CustomUser

admin.site.register(CustomUser, UserAdmin)
