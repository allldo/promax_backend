from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cabinet.models import CustomUser

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        (("Дополнительная информация"), {
            "fields": ("favorite",),
        }),
    )

    list_display = ("id", "email", "phone_number",)
    ordering = ("id", )
    search_fields = ("email", "phone_number",)

admin.site.register(CustomUser, MyUserAdmin)
