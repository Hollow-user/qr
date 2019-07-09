from django.contrib import admin
from .models import *

# Register your models here.


class LectureAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Введите название лекции', {'fields': ['title']}),
        ('Введите дату', {'fields': ['date']}),
        ('Выберите группу', {'fields': ['group']})
                 ]
    list_display = ('title_admin', 'date_admin', 'group_admin', 'stud_come')


class StudentAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Введите имя студента', {'fields': ['name']}),
        ('Выберите группу', {'fields': ['group']}),
        ('Отметьте является ли студент активным', {'fields': ['active']}),
                 ]

    list_display = ('name_admin', 'group_admin', 'active_admin')


admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(Lecture, LectureAdmin)