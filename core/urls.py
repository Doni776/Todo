from django.contrib import admin
from django.urls import path
from main.views import *   # barcha view funksiyalarni import qildik

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Bosh sahifa
    path('', home, name='home'),

    # 2. Hamma studentlar
    path('studentlar/', student_list, name='student_list'),


    # 3. Hamma rejalar
    path('rejalar/', reja_list, name='reja_list'),

    # 4. Bajarilmagan rejalar
    path('bajarilmagan-rejalar/', bajarilmagan_rejalar, name='bajarilmagan_rejalar'),

    # 5. Bitiruvchilar (kurs >= 3)
    path('bitiruvchilar/', bitiruvchilar, name='bitiruvchilar'),

    # 6. Reja o‘chirish
    path('reja/<int:pk>/delete/', reja_delete, name='reja_delete'),


    # 8. Yoshi 20 dan katta studentlar
    path('studentlar/kattalar/', kattalar, name='kattalar'),

    # 9. Bitiruvchilar rejalari
    path('bitiruvchilar/rejalari/', bitiruvchilar_rejalari, name='bitiruvchilar_rejalari'),
    path('talaba/<int:talaba_id>/', student_detail, name='student_detail'),

]
