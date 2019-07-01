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
        id = a['Lecture']
        return redirect('test_id_page', id)


def thx_page(request):
    """Функция для отображения страницы с благодарностью"""
    return render(request, 'testpages/thx.html')


def test_page(request):
    """Функция для отображения страницы с тестом"""

    ls = Lecture.objects.all()

    return render(request, 'testpages/test.html', context={'ls': ls})


def test_id_page(request, id):

    ls = Lecture.objects.get(id__iexact=id)
    students = Students.objects.all()

    if request.method == 'GET':
        return render(request, 'testpages/test.html', context={'ls': ls, 'students': students, 'qr': request.build_absolute_uri()})
    if request.method == 'POST':
        a = request.POST
        print(a['Student'])
        b = Students.objects.get(id__iexact=a['Student'])
        c = Lecture.objects.last()
        c.students_come.add(b)
        return redirect('thx_url')

def qr_generator(request, id):
   a = Lecture.objects.get(id__iexact=id)
   render(request, 'test_id_page', context={'link': request.build_absolute_uri('test/')})