from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to My Todo App!")

def about(request):
    return HttpResponse("This is the About page of Todo App.")

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
