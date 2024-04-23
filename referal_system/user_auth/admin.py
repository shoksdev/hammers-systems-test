from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Регистрируем расширенную модель пользователя в админ-панели"""

    list_display = ('phone_number', 'invite_code', 'auth_code', 'activated_invite_code')
