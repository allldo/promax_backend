from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cabinet.models import CustomUser

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
        (("Дополнительная информация"), {
            "fields": ("favorite",),
        }),
    )

    list_display = ("id", "email", "phone_number",)
    ordering = ("id", )
    search_fields = ("email", "phone_number",)

admin.site.register(CustomUser, MyUserAdmin)
