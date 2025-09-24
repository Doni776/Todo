from django import forms
from main.models import *

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



class RejaForm(forms.ModelForm):
    class Meta:
        model = Reja
        fields = '__all__'
        widgets = {
            'sana': forms.DateInput(attrs={'type': 'date'})
        }




