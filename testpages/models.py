from django.db import models
from django.shortcuts import reverse


class Group(models.Model):

    name = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Группа №{}'.format(self.name)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Lecture(models.Model):

    title = models.CharField(max_length=50)
    date = models.DateField(auto_created=True)
    students_come = models.ManyToManyField('Student', blank=True,
                                           related_name='students',)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        return '{}'.format(self.title)

    def group_admin(self):
        return '{}'.format(self.group)
    group_admin.short_description = 'Группа'

    def title_admin(self):
        return '{}'.format(self.title)
    title_admin.short_description = 'Лекция'

    def date_admin(self):
        return '{}'.format(self.date)
    date_admin.short_description = 'Дата'

    def stud_come(self):
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

    name = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        return '{}'.format(self.name)

    def name_admin(self):
        return '{}'.format(self.name)
    name_admin.short_description = 'Студент'

    def group_admin(self):
        return '{}'.format(self.group)
    group_admin.short_description = 'Группа'

    def active_admin(self):
        if self.active :
            return 'Да'
        else:
            return 'Нет'
    active_admin.short_description = 'Активный'

    class Meta:
        verbose_name = 'Студента'
        verbose_name_plural = 'Студенты'
        ordering = ['group', 'name']

