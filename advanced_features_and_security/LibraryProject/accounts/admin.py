from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.forms import TextInput, Textarea
from django import forms

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # fields shown in admin list
    list_display = ("email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    # fields for creating/editing users
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
