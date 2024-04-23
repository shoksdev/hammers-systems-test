from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user_auth.models import CustomUser
from .serializers import UserProfileSerializer, ActivateInviteCodeSerializer, InvitedUsersSerializer


class UserProfileRetrieveAPIView(RetrieveAPIView):
    """Класс для работы профиля, выводит информацию о текущем пользователе"""

    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_invited_users_view(request):
    """
    Получаем список пользователей, которые ввели инвайт-код пользователя или сообщение
    об отсутствии таких пользователей
    """

    user = request.user

    invited_users = CustomUser.objects.filter(activated_invite_code=user.invite_code)

    if not invited_users.exists():
        return Response({'message': 'Никто не активировал ваш инвайт-код'}, status=status.HTTP_200_OK)

    serializer = InvitedUsersSerializer(invited_users, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def activate_invite_code_view(request):
    """Пользователь вводит инвайт-код другого пользователя для активации"""

    user = request.user

    serializer = ActivateInviteCodeSerializer(data=request.data)
    if serializer.is_valid():
        invite_code = serializer.validated_data['invite_code']

        try:
            existing_user = CustomUser.objects.get(invite_code=invite_code)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Неверный инвайт-код, попробуйте ещё раз!'}, status=status.HTTP_400_BAD_REQUEST)

        if existing_user.activated_invite_code:
            return Response({'error': 'Код приглашения уже активирован, вы не можете иметь более 1 активированного'
                                      ' инвайт-кода на аккаунте!'}, status=status.HTTP_400_BAD_REQUEST)

        if existing_user == user:
            return Response({'error': 'Вы не можете использовать свой инвайт-код для активации!'},
                            status=status.HTTP_400_BAD_REQUEST)

        user.activated_invite_code = invite_code
        user.save()

        return Response({'message': 'Инвайт-код успешно активирован!'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
