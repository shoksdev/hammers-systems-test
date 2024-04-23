from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    """Расширенная модель пользователя"""

    username = models.CharField(max_length=256, unique=False, verbose_name='Имя пользователя')
    invite_code = models.CharField(max_length=6, unique=True, validators=[
        RegexValidator(r'^[a-zA-Z0-9]*$', message='Invite code must consist of letters and numbers')],
                                   verbose_name='Инвайт-код')
    phone_number = models.CharField(max_length=15, unique=True,
                                    validators=[RegexValidator(r'^\+?\d{9,15}$', message='Invalid phone number')],
                                    verbose_name='Номер телефона')
    auth_code = models.CharField(max_length=4, blank=True, null=True, verbose_name='Код аутентификации')
    activated_invite_code = models.CharField(max_length=6, blank=True, null=True,
                                             verbose_name='Активированный инвайт-код')

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email", "username"]
