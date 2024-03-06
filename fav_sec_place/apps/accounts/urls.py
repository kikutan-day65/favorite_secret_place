from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login-user/', views.login_user, name='login-user'),
    path('logout-user/', views.logout_user, name='logout-user'),
]
