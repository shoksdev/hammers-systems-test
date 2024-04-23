from django.urls import path
from .views import request_phone_auth_view, verify_auth_code_view

urlpatterns = [
    path('request/', request_phone_auth_view, name='request_phone_auth'),
    path('verify/', verify_auth_code_view, name='verify_code'),
]
