from rest_framework import serializers

from user_auth.models import CustomUser


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения информации о пользователе в профиле"""

    class Meta:
        model = CustomUser
        fields = ('phone_number', 'invite_code', 'activated_invite_code',)


class ActivateInviteCodeSerializer(serializers.Serializer):
    """Сериализатор для активации инвайт-кода"""

    invite_code = serializers.CharField(max_length=6)


class InvitedUsersSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода всех пользователей (их номеров телефонов), указавших инвайт-код"""

    class Meta:
        model = CustomUser
        fields = ['phone_number']
