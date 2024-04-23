from django.contrib import admin
from django.urls import path, include

from .doc import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('profile/', include('user_profile.urls')),
]

urlpatterns += doc_urls
