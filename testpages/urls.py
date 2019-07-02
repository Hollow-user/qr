from django.contrib import admin
from django.urls import path, include


from .views import *

""" пути к страницам """
urlpatterns = [
    path('', QrPage.as_view(), name='qr_page_url'),
    path('thx/', thx_page, name='thx_url'),
    path('check/', check_page, name='check_url'),
    path('lecture/', LecturePage.as_view(), name='lecture_url'),
    path('test/<int:id>/', TestIdPage.as_view(), name='test_id_page'),
    path('student', StudentPage.as_view(), name='student_page'),
    path('student/<int:id>/', StudentIdPage.as_view(), name='student_id_page'),
    path('qr/<int:id>/', qr_id_page, name='qr_id_page'),
    path('late/', late_page, name='late_url'),


]
