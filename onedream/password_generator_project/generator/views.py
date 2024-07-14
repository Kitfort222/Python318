from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    psw = 'qwerty'
    return render(request, "generator/home.html", {'password': psw, 'title': "Главная страница"})
