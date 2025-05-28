from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from json import dumps

from ..forms import LoginForm, RegisterForm


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'auth/login.html', context={"form": LoginForm()})

    form = LoginForm(request.POST)
    return HttpResponse(dumps({
        "status": "success",
        "message": "Login successful",
        "credentials": {
            "username": form.cleaned_data['username'],
            "password": form.cleaned_data['password']
        }
    }), content_type='application/json')


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'auth/register.html', context={"form": RegisterForm()})

    # Here you would typically handle registration logic
    return HttpResponse(dumps({
        "status": "success",
        "message": "Registration successful"
    }), content_type='application/json')
