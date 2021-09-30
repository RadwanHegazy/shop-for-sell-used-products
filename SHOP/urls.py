from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('auth/',include('shop_auth.urls')),
    path('profile/',include('user_profile.urls')),
    path('chat/',include('chat.urls')),
]
