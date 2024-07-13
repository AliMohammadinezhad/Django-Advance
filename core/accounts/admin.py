from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active")
    list_filter = ("email", "is_superuser", "is_active")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                )
            },
        ),("Group Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },),("Important dates",
            {
                "fields": (
                    "last_login",
                )
            },),
    )
    add_fieldsets = (
        (
            "Create",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        ("User Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            }),
    )


admin.site.register(Profile)