from django.http import HttpResponse


def news(request):
    return HttpResponse("Новости")


def post(request):
    return HttpResponse("Пост")


def forum(request):
    return HttpResponse("Форум")
