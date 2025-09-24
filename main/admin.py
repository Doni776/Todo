from django.contrib import admin
from .models import Student, Reja
from django.contrib.auth.models import Group, User



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "yosh", "kurs")
    search_fields = ("ism",)                  # ismi bo‘yicha qidiruv
    list_filter = ("kurs",)                   # kurs bo‘yicha filter
    list_display_links = ("id", "ism")        # ism linkka aylansin



@admin.register(Reja)
class RejaAdmin(admin.ModelAdmin):
    list_display = ("id", "sarlavha", "batafsil", "sana", "bajarildi", "student")
    list_filter = ("bajarildi", "sana")       # bajarilgan status + sana bo‘yicha filter
    search_fields = ("sarlavha", "student__ism")  # sarlavha va student ismi bo‘yicha qidiruv
    list_display_links = ("id", "sarlavha")   # sarlavha linkka aylansin
    autocomplete_fields = ("student",)        # reja qo‘shishda student qidirish


admin.site.unregister(Group)
admin.site.unregister(User)
