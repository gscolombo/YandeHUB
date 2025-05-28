from django.shortcuts import render
from ..forms.login import LoginForm


def login_form(request):
    return render(request, 'auth/login.html', context={"form": LoginForm()})
