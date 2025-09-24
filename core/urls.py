from django.contrib import admin
from django.urls import path
from main.views import *   # barcha view funksiyalarni import qildik

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Bosh sahifa
    path('', home, name='home'),

    # 2. Hamma studentlar (ism link bo‘ladi)
    path('studentlar/', student_list, name='student_list'),
    path('student/<int:pk>/', student_detail, name='student_detail'),

    # 3. Hamma rejalar (form orqali qo‘shish, yonida o‘chirish)
    path('rejalar/', reja_list, name='reja_list'),
    path('reja/<int:pk>/delete/', reja_delete, name='reja_delete'),

    # 4. Bajarilmagan rejalar
    path('rejalar/bajarilmagan/', bajarilmagan_rejalar, name='bajarilmagan_rejalar'),

    # 5. 3 va 4 kurs talabalar
    path('studentlar/kurs-3-4/', kurs_3_4_students, name='kurs_3_4_students'),

    # 6. Yoshi 20 dan baland talabalar
    path('studentlar/yoshi-20dan-baland/', yoshi_20dan_baland_students, name='yoshi_20dan_baland_students'),

    # 7. Kursi 4 bo‘lgan talabalar
    path('studentlar/kurs-4/', kurs_4_students, name='kurs_4_students'),
]

