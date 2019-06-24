from django.contrib import admin
from django.urls import path, include


from .views import *

""" пути к страницам """
urlpatterns = [
    path('', qr_page, name='qr_page_url'),
    path('thx/', thx_page, name='thx_url'),
    path('lecture/', lecture_page, name='lecture_url'),

]
