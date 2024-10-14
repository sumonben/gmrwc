import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# import GeeksModel from models.py
from teacher.models import Teacher
from .models import Student
from department.models import Department
 
# create a ModelForm
class StudentForm(forms.ModelForm):
    department=forms.ModelMultipleChoiceField(queryset=Department.objects.all(), widget=FilteredSelectMultiple('Student',False, attrs={'row':'2'}))
    class Meta:
        model = Student
        fields = "__all__"
        exclude=['std_id']
        