from django.contrib import admin
from django.urls import path
from main.views import *   # barcha view funksiyalarni import qildik

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', home, name='home'),
    path('studentlar/', student_list, name='student_list'),
    path('student/<int:pk>/', student_detail, name='student_detail'),
    path('rejalar/', reja_list, name='reja_list'),
    path('reja/<int:pk>/delete/', reja_delete, name='reja_delete'),
    path('rejalar/bajarilmagan/', bajarilmagan_rejalar, name='bajarilmagan_rejalar'),
    path('studentlar/kurs-3-4/', kurs_3_4_students, name='kurs_3_4_students'),
    path('studentlar/yoshi-20dan-baland/', yoshi_20dan_baland_students, name='yoshi_20dan_baland_students'),
    path('studentlar/kurs-4/', kurs_4_students, name='kurs_4_students'),
]

