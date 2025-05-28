from django.urls import path
from .views.auth import login_form

urlpatterns = [
    path('auth/', login_form, name='login_page')
]
