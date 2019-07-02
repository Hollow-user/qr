from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, response
from django.views.generic import View
from .utils import PageMixin
from .models import *


class QrPage(View):
    """Функция для отображения страницы с кр кодом"""
    def get(self, request):
        lectures = reversed(Lecture.objects.all())
        return render(request, 'testpages/qr_page.html', context={'lectures': lectures})

    def post(self, request):
        a = request.POST
        id = a['Lecture']
        return redirect('qr_id_page', id)


class LecturePage(View):
    """Функция для отображения страницы с лекциями"""
    def get(self, request):
        lectures = reversed(Lecture.objects.all())
        return render(request, 'testpages/lecture.html', context={'lectures': lectures})

    def post(self, request):
        a = request.POST
        id = a['Lecture']
        return redirect('test_id_page', id)


class TestIdPage(View):
    """Функция для отображения страницы с лекцией"""
    def get(self, request, id):
        ls = get_object_or_404(Lecture, id__iexact=id)
        students = Student.objects.all()
        return render(request, 'testpages/test.html', context={'ls': ls, 'students': students, 'qr': request.build_absolute_uri()})

    def post(self, request, id):
        if request.session.get('check', False):
            return redirect('check_url')
        else:
            if len(Lecture.objects.values('students_come').filter(id__iexact=id)) < Lecture.objects.get(id=id).count:
                request.session['check'] = True
                print(request.COOKIES)
                request.session.set_expiry(86400)
                a = request.POST
                b = get_object_or_404(Student, id__iexact=a['Student'])
                c = get_object_or_404(Lecture, id__iexact=id)
                c.students_come.add(b)
                return redirect('thx_url')
            else:
                chislo = len(Lecture.objects.values('students_come').filter(id__iexact=id))
                print(chislo)
                return redirect('late_url')


class StudentPage(View):
    """Функция показывает список студентов """
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'testpages/student.html', context={'students': students})

    def post(self, request):
        a = request.POST
        id = a['Student']
        return redirect('student_id_page', id)


class StudentIdPage(View):
    """Функция показывает посещенные лекции студента """
    def get(self, request, id):
        lectures = get_object_or_404(Student, id__iexact=id).students.all()
        student = get_object_or_404(Student, id__iexact=id)
        return render(request, 'testpages/student_id.html', context={'lectures': lectures, 'student': student})

    def post(self, request, id):
        a = request.POST
        id = a['Lecture']
        return redirect('test_id_page', id)


def qr_id_page(request, id):
    """Функция показывает qr code для определенной лекции """
    ls = get_object_or_404(Lecture, id__iexact=id)
    qr = 'http://127.0.0.1:8000/test/' + str(id) + '/'
    return render(request, 'testpages/qr_id_page.html', context={'qr': qr, 'ls': ls})


def qr_generator(request, id):
    """Функция для отображения кр кода для определенной лекции (только для страницы с самой лекцией"""
    render(request, 'test_id_page', context={'link': request.build_absolute_uri('test/')})


class ThxPage(PageMixin, View):
    """Функция для отображения страницы с благодарностью"""
    template = 'testpages/thx.html'


class LatePage(PageMixin, View):
    """Функция для отображения страницы с опозданием"""
    template = 'testpages/late.html'


class CheckPage(PageMixin, View):
    """Функция для отображения страницы с отказом"""
    template = 'testpages/check.html'
