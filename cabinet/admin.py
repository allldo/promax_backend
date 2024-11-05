from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cabinet.models import CustomUser

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (("Дополнительная информация"), {
            "fields": ("phone_number", "favorite"),
        }),
    )

    list_display = UserAdmin.list_display + ("phone_number",)

    search_fields = UserAdmin.search_fields + ("phone_number",)

admin.site.register(CustomUser, MyUserAdmin)
