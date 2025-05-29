from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
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
    errors = ["E-mail inválido!"]
    if request.method == 'GET':
        return render(request, 'auth/register.html', context={"form": RegisterForm()})

    assert request.method == 'POST', "Invalid request method"

    form = RegisterForm(request.POST)
    return JsonResponse({
        "status": "error",
        "message": "Registration failed",
        "errors": errors
    }, status=400)
