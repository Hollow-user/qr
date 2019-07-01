from django.db import models
from django.shortcuts import reverse


class Students(models.Model):

    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '{}'.format(self.name)


class Lecture(models.Model):

    title = models.CharField(max_length=50)
    date = models.DateField(auto_created=True)
    students_come = models.ManyToManyField('Students', blank=True, related_name='students',)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('lecture_detail_url', kwargs={'id': self.id})
