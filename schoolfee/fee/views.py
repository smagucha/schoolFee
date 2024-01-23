from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("This is a school fee management system")
