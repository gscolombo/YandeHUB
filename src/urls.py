from django.urls import path
from .views.auth import login, register, recover_password

urlpatterns = [
    path('auth/login', login, name='login'),
    path('auth/register', register, name='register'),
    path('auth/recover', recover_password, name='recover_password')
]
