from django.contrib import admin
from .models import *

# Настройка отображения моделей в админке


class LectureAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Введите название лекции', {'fields': ['title']}),
        ('Введите дату', {'fields': ['date']}),
        ('Выберите группу', {'fields': ['group']}),
        ('Список студентов', {'fields': ['students_come']})
                 ]
    filter_horizontal = ['students_come']
    list_display = ('title', 'date', 'group', 'stud_come')
    search_fields = ['title']
    list_filter = ['title', 'date', 'group']


class LectureInline(admin.TabularInline):

    model = Lecture.students_come.through
    extra = 0


class StudentAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Введите имя студента', {'fields': ['name']}),
        ('Выберите группу', {'fields': ['group']}),
        ('Отметьте является ли студент активным', {'fields': ['active']}),
                 ]

    list_display = ('name', 'group', 'active_admin')
    search_fields = ['name']
    list_filter = ['group', 'active']
    inlines = [LectureInline]


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'


class GroupAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_filter = ['name']
    list_display = ['name', 'count_group']
    fieldsets = [
        ('Введите имя группы', {'fields': ['name']}),

    ]
    inlines = [StudentInline]

# Регистрация моделей в админке


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Lecture, LectureAdmin)