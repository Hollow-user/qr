from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator
from datetime import date
from .utils import PageMixin
from .models import *


class QrPage(View):
    """Отображение страницы с кр кодом"""
    def get(self, request):
        lectures = Lecture.objects.filter(date=date.today())
        return render(request, 'testpages/qr_page.html',
                      context={'lectures': lectures})

    def post(self, request):
        return redirect('qr_id_page', request.POST['Lecture'])


class LecturePage(View):
    """Отображение страницы с лекциями"""
    def get(self, request):
        lectures = Lecture.objects.all()
        pagitanor = Paginator(lectures, 4)
        page_number = request.GET.get('page', 1)
        page = pagitanor.get_page(page_number)
        is_paginator = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        context = {
            'lectures': page,
            'prev_url': prev_url,
            'next_url': next_url,
            'is_paginator': is_paginator
        }
        return render(request, 'testpages/lecture.html',
                      context=context)

    def post(self, request):
        a = request.POST
        return redirect('lecture_id_page', a['Lecture'])


class LectureIdPage(View):
    """Отображение страницы с лекцией"""
    def get(self, request, id):
        ls = get_object_or_404(Lecture, id__iexact=id)
        students = Student.objects.filter(active=True, group=ls.group.id)
        return render(request, 'testpages/lecture_id.html',
                      context={'ls': ls, 'students': students})

    def post(self, request, id):
        if Lecture.objects.dates('date', 'day').get(id=id) != date.today():
            return redirect('date_late_url')
        else:
            if request.session.get('check', False):
                return redirect('check_url')
            else:
                request.session['check'] = True
                request.session.set_expiry(86400)
                a = request.POST
                b = get_object_or_404(Student, id__iexact=a['Student'])
                c = get_object_or_404(Lecture, id__iexact=id)
                c.students_come.add(b)
                return redirect('thx_url')


class StudentPage(View):
    """Отображение списка студентов """
    def get(self, request):
        students = Student.objects.all()
        pagitanor = Paginator(students, 4)
        page_number = request.GET.get('page', 1)
        page = pagitanor.get_page(page_number)
        is_paginator = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        context = {
            'students': page,
            'prev_url': prev_url,
            'next_url': next_url,
            'is_paginator': is_paginator
        }
        return render(request, 'testpages/student.html',
                      context=context)

    def post(self, request):
        return redirect('student_id_page', request.POST['Student'])


class StudentIdPage(View):
    """Список посещенных лекций студента """
    def get(self, request, id):
        lectures = get_object_or_404(Student, id__iexact=id).students.all()
        student = get_object_or_404(Student, id__iexact=id)
        pagitanor = Paginator(lectures, 4)
        page_number = request.GET.get('page', 1)
        page = pagitanor.get_page(page_number)
        is_paginator = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        return render(request, 'testpages/student_id.html',
                      context={'student': student,
                               'lectures': page,
                               'prev_url': prev_url,
                               'next_url': next_url,
                               'is_paginator': is_paginator
                               })

    def post(self, request, id):
        return redirect('lecture_id_page', request.POST['Lecture'])


def qr_id_page(request, id):
    """Отображение qr code для определенной лекции """
    ls = get_object_or_404(Lecture, id__iexact=id)
    qr = request.build_absolute_uri('lecture/')
    return render(request, 'testpages/qr_id_page.html',
                  context={'qr': qr, 'ls': ls})


class ThxPage(PageMixin, View):
    """Вывод страницы если студент отметился"""
    message = 'Спасибо что отметились'


class DateLatePage(PageMixin, View):
    """Вывод страницы если студент пытается отметиться за прошедшую дату"""
    message = 'Вы пытаетесь отметится за прошедшую дату'


class CheckPage(PageMixin, View):
    """Вывод страницы если студент уже сегодня отмечался"""
    message = 'Вы уже отмечались сегодня'




