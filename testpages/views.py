from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def qr_page(request):
    """Функция для отображения страницы с кр кодом"""
    return render(request, 'testpages/qr_page.html')


def lecture_page(request):
    """Функция для отображения страницы с лекциями"""
    lectures = reversed(Lecture.objects.all())
    if request.method == 'GET':
        return render(request, 'testpages/lecture.html', context={'lectures': lectures})
    if request.method == 'POST':
        a = request.POST
        c = Lecture.objects.get(id=a['Лекция']).visiters
        Lecture.objects.filter(id=a['Лекция']).update(visiters=c+1)
        return redirect('thx_url')


def thx_page(request):
    """Функция для отображения страницы с благодарностью"""
    return render(request, 'testpages/thx.html')


