import random
import string
import time

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import PhoneAuthSerializer, CodeVerificationSerializer


def generate_code(code_len, code_type):
    """Генерируем код указанной длины из случайных элементов по усмотрению (букв, цифр, все вместе)"""

    if code_type == 'letters':
        invite_code_elements = string.ascii_letters
    elif code_type == 'digits':
        invite_code_elements = string.digits
    else:
        invite_code_elements = string.ascii_letters + string.digits

    code = ''.join(random.choices(invite_code_elements, k=code_len))
    return code


@api_view(['POST'])
def request_phone_auth_view(request):
    """Первая часть авторизации, пользователь вводит номер телефона и программа имитирует отправку сообщения"""

    serializer = PhoneAuthSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']

        user, created_flag = CustomUser.objects.get_or_create(phone_number=phone_number)

        if created_flag:
            invite_code = generate_code(code_len=6, code_type='all')
            user.invite_code = invite_code
            user.save()

        auth_code = generate_code(code_len=4, code_type='digits')

        user.auth_code = auth_code
        user.save()

        time.sleep(random.randint(1, 2))

        return Response({'message': 'Код авторизации отправлен, проверьте телефон!'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_auth_code_view(request):
    """
    Вторая часть авторизации, пользователь вводит аутентификационный код,
    подтверждает свой номер телефона и получает токен для авторизации
    """

    serializer = CodeVerificationSerializer(data=request.data)
    if serializer.is_valid():
        auth_code = serializer.validated_data['auth_code']

        try:
            user = CustomUser.objects.get(auth_code=auth_code)
            user.auth_code = ''
            user.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'message': 'Авторизация прошла успешно, добро пожаловать!', 'token': access_token},
                            status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Неверный код авторизации, попробуйте ещё раз!'},
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
