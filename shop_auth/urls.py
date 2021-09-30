from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]