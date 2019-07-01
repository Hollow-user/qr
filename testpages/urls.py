from django.contrib import admin
from django.urls import path, include


from .views import *

""" пути к страницам """
urlpatterns = [
    path('', qr_page, name='qr_page_url'),
    path('thx/', thx_page, name='thx_url'),
    path('check/', check_page, name='check_url'),
    path('lecture/', lecture_page, name='lecture_url'),
    path('test/', test_page, name='test_url'),
    path('test/<int:id>/', test_id_page, name='test_id_page'),


]
