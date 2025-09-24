from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User

admin.site.register(Student)
admin.site.register(Reja)

admin.site.unregister(Group)
admin.site.unregister(User)

class RejaAdmin(admin.ModelAdmin):
    list_display = ("id","sarlavha", "batadsil",  "sana", "bajarildi", "student"  )
    list_filter = ("bajarildi",  )
    list_display_links = ("id", "sarlavha")
