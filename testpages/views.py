from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

def qr_page(request):
    return render(request, 'testpages/qr_page.html')

# Функция для отображения страницы с кр кодом

def lecture_page(request):

    lectures = reversed(Lecture.objects.all())
    if request.method == 'GET':

        return render(request, 'testpages/lecture.html', context={'lectures': lectures})
    if request.method == 'POST':
        a = request.POST
        c = Lecture.objects.get(id=a['Лекция']).visiters
        Lecture.objects.filter(id=a['Лекция']).update(visiters=c+1)

        print(c)






        return redirect('thx_url')

# Функция для отображения страницы с лекциями

def thx_page(request):

    return render(request, 'testpages/thx.html')

# Функция для отображения страницы с благодарностью
