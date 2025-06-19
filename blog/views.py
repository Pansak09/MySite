from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    response = HttpResponse('Blog home')
    return response