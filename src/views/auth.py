from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from json import dumps

from ..forms import LoginForm, RegisterForm, RecoverPasswordForm


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

    assert request.method == 'POST', "Invalid request method"

    return JsonResponse({})


def recover_password(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'auth/recover_password.html', context={"form": None})

    assert request.method == 'POST', "Invalid request method"

    return JsonResponse({})
