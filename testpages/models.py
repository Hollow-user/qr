from django.db import models

# Create your models here.

class Lecture(models.Model):

    title = models.CharField(max_length=50)
    date = models.DateField(auto_created=True)
    visiters = models.BigIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.title)

# Модель для создания лекций