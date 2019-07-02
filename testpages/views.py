from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import *


def qr_page(request):
    """Функция для отображения страницы с кр кодом"""
    lectures = reversed(Lecture.objects.all())
    if request.method == 'GET':
        return render(request, 'testpages/qr_page.html', context={'lectures': lectures})
    if request.method == 'POST':
        a = request.POST
        id = a['Lecture']
        return redirect('qr_id_page', id)


def lecture_page(request):
    """Функция для отображения страницы с лекциями"""
    lectures = reversed(Lecture.objects.all())
    if request.method == 'GET':
        return render(request, 'testpages/lecture.html', context={'lectures': lectures})
    if request.method == 'POST':
        a = request.POST
        id = a['Lecture']
        return redirect('test_id_page', id)


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
            if len(Lecture.objects.values('students_come').filter(id__iexact=id)) < Lecture.objects.get(id=id).count:
                request.session['check'] = True
                print(request.COOKIES)
                request.session.set_expiry(86400)
                a = request.POST
                b = Student.objects.get(id__iexact=a['Student'])
                c = Lecture.objects.get(id__iexact=id)
                c.students_come.add(b)
                return redirect('thx_url')
            else:
                chislo = len(Lecture.objects.values('students_come').filter(id__iexact=id))
                print(chislo)
                return redirect('late_url')


def student_page(request):
    """Функция для отображения списка студентов"""
    students = Student.objects.all()
    if request.method == 'GET':
        return render(request, 'testpages/student.html', context={'students': students})
    if request.method == 'POST':
        a = request.POST
        id = a['Student']
        return redirect('student_id_page', id)


def student_id_page(request, id):
    """Функция показывает посещенные лекции студента """
    if request.method == 'GET':
        lectures = Student.objects.get(id__iexact=id).students.all()
        student = Student.objects.get(id__iexact=id)
        return render(request, 'testpages/student_id.html', context={'lectures': lectures, 'student': student})
    if request.method == 'POST':
        a = request.POST
        id = a['Lecture']
        return redirect('test_id_page', id)


def qr_id_page(request, id):
    """Функция показывает qr code для определенной лекции """
    ls = Lecture.objects.get(id__iexact=id)
    qr = 'http://127.0.0.1:8000/test/' + str(id) + '/'
    return render(request, 'testpages/qr_id_page.html', context={'qr': qr, 'ls': ls})


def qr_generator(request, id):
    """Функция для отображения кр кода для определенной лекции (только для страницы с самой лекцией"""
    render(request, 'test_id_page', context={'link': request.build_absolute_uri('test/')})


def thx_page(request):
    """Функция для отображения страницы с благодарностью"""
    return render(request, 'testpages/thx.html')


def late_page(request):
    """Функция для отображения страницы с опозданием"""
    return render(request, 'testpages/late.html')


def check_page(request):
    """Функция для отображения страницы с отказом"""
    return render(request, 'testpages/check.html')
