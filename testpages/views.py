from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
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
        search_query = request.GET.get('search', '')
        if search_query:
            search_paginator = True
            lectures = Lecture.objects.filter(
                Q(title__icontains=search_query) |
                Q(group__name__icontains=search_query) |
                Q(date__icontains=search_query)

            )
        else:
            search_paginator = False
            lectures = Lecture.objects.all()
        pagitanor = Paginator(lectures, 4)
        page_number = request.GET.get('page', 1)
        page = pagitanor.get_page(page_number)
        is_paginator = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
            prev_url_search = '?search={}&page={}'.format(
                search_query,
                page.previous_page_number()
            )
        else:
            prev_url = ''
            prev_url_search = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
            next_url_search = '?search={}&page={}'.format(
                search_query,
                page.next_page_number()
            )
        else:
            next_url = ''
            next_url_search = ''
        context = {
            'lectures': page,
            'prev_url': prev_url,
            'next_url': next_url,
            'is_paginator': is_paginator,
            'search_query': search_query,
            'search_paginator': search_paginator,
            'prev_url_search': prev_url_search,
            'next_url_search': next_url_search,
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
                request.session.set_expiry(3600)
                a = request.POST
                b = get_object_or_404(Student, id__iexact=a['Student'])
                c = get_object_or_404(Lecture, id__iexact=id)
                c.students_come.add(b)
                return redirect('thx_url')


class GroupPage(View):
    """ Вывод страницы с группами"""
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            search_paginator = True
            groups = Group.objects.filter(Q(name__icontains=search_query))
        else:
            search_paginator = False
            groups = Group.objects.all()
        pagitanor = Paginator(groups, 4)
        page_number = request.GET.get('page', 1)
        page = pagitanor.get_page(page_number)
        is_paginator = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
            prev_url_search = '?search={}&page={}'.format(
                search_query,
                page.previous_page_number()
            )
        else:
            prev_url = ''
            prev_url_search = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
            next_url_search = '?search={}&page={}'.format(
                search_query,
                page.next_page_number()
            )
        else:
            next_url = ''
            next_url_search = ''
        context = {
                   'groups': page,
                   'prev_url': prev_url,
                   'next_url': next_url,
                   'is_paginator': is_paginator,
                   'search_paginator': search_paginator,
                   'search_query': search_query,
                   'prev_url_search': prev_url_search,
                   'next_url_search': next_url_search,
                   }
        return render(request, 'testpages/group.html', context=context)

    def post(self, request):
        return redirect('group_id_page', request.POST['Group'])


class GroupIdPage(View):
    """ Вывод страницы со студентами группы"""
    def get(self, request, id):
        students = Student.objects.filter(group=id).order_by('-active', 'name')
        group = Group.objects.get(id=id)
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
            'group': group,
            'prev_url': prev_url,
            'next_url': next_url,
            'is_paginator': is_paginator
        }
        return render(request, 'testpages/group_id.html', context=context)

    def post(self, request, id):
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
    """Вывод страницы если студент пытается отметиться за другую дату"""
    message = 'Отметится можно только в день проведения лекции'


class CheckPage(PageMixin, View):
    """Вывод страницы если студент уже сегодня отмечался"""
    message = 'Вы уже отмечались сегодня'




