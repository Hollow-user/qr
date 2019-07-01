from django.shortcuts import render, redirect
from django.http import HttpResponse, response
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


def check_page(request):
    """Функция для отображения страницы с отказом"""
    return render(request, 'testpages/check.html')


def test_page(request):
    """Функция для отображения страницы с тестом"""
    ls = Lecture.objects.all()
    return render(request, 'testpages/test.html', context={'ls': ls})


def test_id_page(request, id):
    """Функция которая проверяет отметился ли студент или отмечает его"""
    ls = Lecture.objects.get(id__iexact=id)
    students = Student.objects.all()
    if request.method == 'GET':
        return render(request, 'testpages/test.html', context={'ls': ls, 'students': students, 'qr': request.build_absolute_uri()})
    if request.method == 'POST':
        if request.session.get('check', False):
            return redirect('check_url')
        else:
            request.session['check'] = True
            print(request.COOKIES)
            request.session.set_expiry(86400)
            a = request.POST
            b = Student.objects.get(id__iexact=a['Student'])
            c = Lecture.objects.get(id__iexact=id)
            c.students_come.add(b)
            return redirect('thx_url')


def qr_generator(request, id):
   """Функция для отображения кр кода для определенной лекции"""
   render(request, 'test_id_page', context={'link': request.build_absolute_uri('test/')})

