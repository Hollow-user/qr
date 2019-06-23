from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', qr_page, name='qr_page_url'), # страница с кр кодом
    path('thx/',thx_page,name='thx_url'), # страничка с благодарностью
    path('lecture/', lecture_page, name='lecture_url'), # страница с лекциями


]