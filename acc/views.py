from django.http import HttpResponse


def login(request):
    return HttpResponse("Вход")


def registration(request):
    return HttpResponse("Регистрация")


def Featured(request):
    return HttpResponse("Избраное")