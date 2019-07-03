from django.db import models
from django.shortcuts import reverse


class Student(models.Model):

    name = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lecture(models.Model):

    title = models.CharField(max_length=50)
    date = models.DateField(auto_created=True)
    count = models.PositiveIntegerField(default=0)
    students_come = models.ManyToManyField('Student', blank=True,
                                           related_name='students',)

    def __str__(self):
        return str(self.title) + ' ' + '('+str(self.id) + ')'

    def get_absolute_url(self):
        return reverse('lecture_detail_url', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'
