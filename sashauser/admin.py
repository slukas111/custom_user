from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    # model = CustomUser
    list_display = ("display_name",)
    list_filter = ("display_name",)
    fieldsets = (
        (None, {"fields": ("username", "display_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
