from django.urls import path
from .views.auth import login, register, recover_password, set_new_password

urlpatterns = [
    path('auth/login', login, name='login'),
    path('auth/register', register, name='register'),
    path('auth/recover', recover_password, name='recover_password'),
    path('recover_password', set_new_password, name='set_new_password')
]
