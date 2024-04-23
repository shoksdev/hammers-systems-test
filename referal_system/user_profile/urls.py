from django.urls import path
from .views import UserProfileRetrieveAPIView, activate_invite_code_view, get_invited_users_view

urlpatterns = [
    path('', UserProfileRetrieveAPIView.as_view(), name='profile'),
    path('invited_users/', get_invited_users_view, name='invited_users'),
    path('activate_invite_code/', activate_invite_code_view, name='activate_invite_code'),
]

