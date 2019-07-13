from django.db import models
from django.shortcuts import reverse


class Group(models.Model):
    """ Модель группа"""
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return 'Группа {}'.format(self.name)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Lecture(models.Model):
    """ Модель лекция"""
    title = models.CharField(max_length=50)
    date = models.DateField(auto_created=True)
    students_come = models.ManyToManyField('Student', blank=True,
                                           related_name='students',)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}'.format(self.title)

    def group_admin(self):
        return '{}'.format(self.group)
    group_admin.short_description = 'Группа'
    group_admin.admin_order_field = 'group'

    def title_admin(self):
        return '{}'.format(self.title)
    title_admin.short_description = 'Лекция'

    def date_admin(self):
        return self.date
    date_admin.short_description = 'Дата'
    date_admin.admin_order_field = 'date'

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
    name = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}'.format(self.name)

    def name_admin(self):
        return '{}'.format(self.name)
    name_admin.short_description = 'Студент'
    name_admin.admin_order_field = 'name'

    def group_admin(self):
        return '{}'.format(self.group)
    group_admin.short_description = 'Группа'
    group_admin.admin_order_field = 'group'

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

