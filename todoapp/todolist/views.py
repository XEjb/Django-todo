from django.http import HttpResponse
from django.shortcuts import render

from .models import ToDo


def index(request):
    todo = ToDo.objects.all()
    return HttpResponse('Helloo o o o o o o o o o o o o o o o o o o o o o o o o')
