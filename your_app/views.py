from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to My Todo App!")

def about(request):
    return HttpResponse("This is the About page of Todo App.")

