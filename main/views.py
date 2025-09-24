from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def home(request):
    return render(request, "home.html")

# 1. Hamma studentlarni chiqarish + ismi link bo‘lsin
def student_list(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "student_list.html", context)

# Student detail (bosilganda rejalari chiqsin)
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    rejalari = Reja.objects.filter(student=student)
    context = {"student": student, "rejalari": rejalari}
    return render(request, "student_detail.html", context)

# 2. Hamma rejalar + pastda form orqali yangi reja qo‘shish + yonida o‘chirish
def reja_list(request):
    rejalari = Reja.objects.select_related("student").all()

    if request.method == "POST":
        form = RejaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reja_list")
    else:
        form = RejaForm()

    context = {"rejalari": rejalari, "form": form}
    return render(request, "reja_list.html", context)

# Rejani o‘chirish
def reja_delete(request, pk):
    reja = get_object_or_404(Reja, pk=pk)
    reja.delete()
    return redirect("reja_list")

# 3. Bajarilmagan rejalar
def bajarilmagan_rejalar(request):
    rejalari = Reja.objects.filter(bajarildi=False)
    context = {"rejalari": rejalari}
    return render(request, "bajarilmagan_rejalar.html", context)

# 4. 3 va 4 kurs talabalar
def kurs_3_4_students(request):
    students = Student.objects.filter(kurs__in=[3, 4])
    context = {"students": students}
    return render(request, "kurs_3_4_students.html", context)

# 5. Yoshi 20 dan baland talabalar
def yoshi_20dan_baland_students(request):
    students = Student.objects.filter(yosh__gt=20)
    context = {"students": students}
    return render(request, "yoshi_20dan_baland_students.html", context)

# 6. Kursi 4 bo‘lgan talabalar
def kurs_4_students(request):
    students = Student.objects.filter(kurs=4)
    context = {"students": students}
    return render(request, "kurs_4_students.html", context)
