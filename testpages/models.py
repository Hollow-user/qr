from django.db import models


class Lecture(models.Model):
    """ Модель для создания лекций """

    title = models.CharField(max_length=50)
    date = models.DateField(auto_created=True)
    visiters = models.BigIntegerField(default=0)

    """ Переопределение метода строки для вывода моделей """
    def __str__(self):
        return '{}'.format(self.title)