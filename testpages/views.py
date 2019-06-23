from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def qr_page(request):
    return render(request, 'testpages/qr_page.html')

# Функция для отображения страницы с кр кодом

def lecture_page(request):

    lectures = Lecture.objects.all()

    return render(request, 'testpages/lecture.html', context={'lectures':lectures})

# Функция для отображения страницы с лекциями

def thx_page(request):
    return render(request, 'testpages/thx.html')

# Функция для отображения страницы с благодарностью
