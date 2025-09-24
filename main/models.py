from django.db import models

class Student(models.Model):
    ism=models.CharField(max_length=255)
    yosh=models.IntegerField()
    kurs=models.IntegerField()

    def __str__(self):
        return self.ism

class Reja(models.Model):
    sarlavha=models.TextField()
    batafsil=models.TextField(null=True)
    sana=models.DateTimeField(auto_now_add=True)
    bajarildi=models.BooleanField(default=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha

