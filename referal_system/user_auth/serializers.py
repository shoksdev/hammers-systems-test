from rest_framework import serializers


class PhoneAuthSerializer(serializers.Serializer):
    """Сериализатор для начала авторизации (получение номера телефона)"""

    phone_number = serializers.CharField(max_length=15)


class CodeVerificationSerializer(serializers.Serializer):
    """Сериализатор для верификации номера телефона и ввода аутентификационного кода"""

    auth_code = serializers.CharField(max_length=4)
