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
        return str(self.title) + ' ' + '('+str(self.id) + ')'

    def get_absolute_url(self):
        return reverse('lecture_detail_url', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'


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

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
