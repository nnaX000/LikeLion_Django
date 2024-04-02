from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    list_display = ("email", "name", "is_staff")  # 'username' 대신 'email'을 사용
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "name")
    ordering = ("email",)  # 'username' 대신 'email'로 정렬

    # 필드셋 설정도 여러분의 모델에 맞게 조정해야 할 수 있습니다.
    # 예를 들어, 'username' 필드 대신 'email' 필드를 사용하도록 아래의 필드셋을 조정합니다.
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("name",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
