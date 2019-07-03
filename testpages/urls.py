from django.contrib import admin
from django.urls import path, include


from .views import *

""" пути к страницам """
urlpatterns = [
    path('', QrPage.as_view(), name='qr_page_url'),
    path('thx/', ThxPage.as_view(), name='thx_url'),
    path('check/', CheckPage.as_view(), name='check_url'),
    path('lecture/', LecturePage.as_view(), name='lecture_url'),
    path('test/<int:id>/', TestIdPage.as_view(), name='test_id_page'),
    path('student', StudentPage.as_view(), name='student_page'),
    path('student/<int:id>/', StudentIdPage.as_view(), name='student_id_page'),
    path('qr/<int:id>/', qr_id_page, name='qr_id_page'),
    path('late/', LatePage.as_view(), name='late_url'),
    path('datelate/', DateLatePage.as_view(), name='date_late_url'),


]
