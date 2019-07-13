from django.urls import path


from .views import *

""" пути к страницам """
urlpatterns = [
    path('', QrPage.as_view(), name='qr_page_url'),
    path('lecture/', LecturePage.as_view(), name='lecture_url'),
    path('qr/<int:id>/', qr_id_page, name='qr_id_page'),
    path('qr/<int:id>/lecture/', LectureIdPage.as_view(), name='lecture_id_page'),
    path('student', StudentPage.as_view(), name='student_page'),
    path('student/<int:id>/', StudentIdPage.as_view(), name='student_id_page'),
    path('datelate/', DateLatePage.as_view(), name='date_late_url'),
    path('thx/', ThxPage.as_view(), name='thx_url'),
    path('check/', CheckPage.as_view(), name='check_url'),


]
