from django.db import models
from django.shortcuts import reverse


class Group(models.Model):
    """ Модель группа"""
    name = models.CharField(max_length=30, unique=True, verbose_name='Группа')

    def __str__(self):
        return 'Группа {}'.format(self.name)

    def count_group(self):
        return self.student_set.count()
    count_group.short_description = 'Количество студентов'

    def stud_admin(self):
        return self.student_set

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Lecture(models.Model):
    """ Модель лекция"""
    title = models.CharField(max_length=50, verbose_name='Лекция')
    date = models.DateField(auto_created=True, verbose_name='Дата')
    students_come = models.ManyToManyField('Student', blank=True,
                                           related_name='students',)
    group = models.ForeignKey(
        Group, verbose_name='Группа',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}'.format(self.title)

    def stud_come(self):
        """ Отображение числа пришедших студентов из группы"""
        a = self.students_come.count()
        b = self.group.student_set.filter(active=True).values().count()
        return str(a) + ' из ' + str(b)
    stud_come.short_description = 'Студентов пришло'

    def get_absolute_url(self):
        return reverse('lecture_detail_url', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Лекцию'
        verbose_name_plural = 'Лекции'
        ordering = ['-date']


class Student(models.Model):
    """ Модель студент"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Имя')
    active = models.BooleanField(default=True, verbose_name='Активность')
    group = models.ForeignKey(
        Group, verbose_name='Группа',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}'.format(self.name)

    def active_admin(self):
        if self.active:
            return 'Да'
        else:
            return 'Нет'
    active_admin.short_description = 'Активный'
    active_admin.admin_order_field = 'active'

    class Meta:
        verbose_name = 'Студента'
        verbose_name_plural = 'Студенты'
        ordering = ['group', 'name']

