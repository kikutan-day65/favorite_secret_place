from django.urls import path
from . import views


urlpatterns = [
    path('login-register/', views.login_register, name='login-register'),
]
