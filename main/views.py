from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Reja
from .forms import StudentsForm, RejaForm


def home(request):
    return render(request, "home.html")


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentsForm()
    return render(request, "student_form.html", {"form": form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentsForm(instance=student)
    return render(request, "student_form.html", {"form": form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_list")


def reja_list(request):
    rejalar = Reja.objects.select_related("student").all()
    return render(request, "reja_list.html", {"rejalar": rejalar})


def reja_create(request):
    if request.method == "POST":
        form = RejaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reja_list")
    else:
        form = RejaForm()
    return render(request, "reja_form.html", {"form": form})


def reja_update(request, pk):
    reja = get_object_or_404(Reja, pk=pk)
    if request.method == "POST":
        form = RejaForm(request.POST, instance=reja)
        if form.is_valid():
            form.save()
            return redirect("reja_list")
    else:
        form = RejaForm(instance=reja)
    return render(request, "reja_form.html", {"form": form})


def reja_delete(request, pk):
    reja = get_object_or_404(Reja, pk=pk)
    reja.delete()
    return redirect("reja_list")





def bajarilmagan_rejalar(request):
    rejalar = Reja.objects.filter(bajarildi=False)
    return render(request, "reja_list.html", {"rejalar": rejalar})


def bitiruvchilar(request):
    students = Student.objects.filter(kurs__gte=3)
    return render(request, "student_list.html", {"students": students})


def kattalar(request):
    students = Student.objects.filter(yosh__gt=20)
    return render(request, "student_list.html", {"students": students})


def bitiruvchilar_rejalari(request):
    rejalar = Reja.objects.filter(student__kurs__gte=3)
    return render(request, "reja_list.html", {"rejalar": rejalar})


def talaba_rejalari(request, talaba_id):
    student = get_object_or_404(Student, pk=talaba_id)
    rejalar = Reja.objects.filter(student=student)
    return render(request, "reja_list.html", {"rejalar": rejalar, "student": student})

def student_detail(request, talaba_id):
    student = get_object_or_404(Student, id=talaba_id)
    return render(request, 'student_detail.html', {'student': student})
