from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("<h1>home</h1>")


def about(request):
    return JsonResponse({"About": "Shaqayeq"})


def contact(request):
    return HttpResponse("Contact")
