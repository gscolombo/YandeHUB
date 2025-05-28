from django.urls import path
from .views.auth import login_form, login

urlpatterns = [
    path('auth/', login_form, name='login_page'),
    path('auth/login', login, name='login')
]
