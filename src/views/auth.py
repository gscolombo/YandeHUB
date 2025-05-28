from django.shortcuts import render
from django.http import HttpResponse
from json import dumps

from ..forms.login import LoginForm


def login_form(request):
    return render(request, 'auth/login.html', context={"form": LoginForm()})


def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        return HttpResponse(dumps({
            "status": "success",
            "message": "Login successful",
            "credentials": {
                "username": form.cleaned_data['username'],
                "password": form.cleaned_data['password']
            }
        }), content_type='application/json')
    return HttpResponse(dumps({
        "status": "error",
        "message": "Invalid credentials"
    }), content_type='application/json')
