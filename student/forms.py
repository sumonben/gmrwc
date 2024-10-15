import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# import GeeksModel from models.py
from teacher.models import Teacher
from .models import Student,SubjectChoice
from department.models import Department
 
# create a ModelForm
class StudentForm(forms.ModelForm):
    department=forms.ModelMultipleChoiceField(Department.objects.all(), widget=FilteredSelectMultiple('Student',False, attrs={'row':'2'}))
    class Meta:
        model = Student
        fields = "__all__"
        exclude=['std_id']
    
class SubjectChoiceForm(forms.ModelForm):
    compulsory_subject=forms.ModelMultipleChoiceField(Department.objects.all(),initial=Department.objects.filter(serial__in=[ 1, 2,3]), widget=FilteredSelectMultiple('Compulsory Subject',False, attrs={'row':'2'}))
    optional_subject=forms.ModelMultipleChoiceField(Department.objects.all(), widget=FilteredSelectMultiple('Optional Subject',False, attrs={'row':'2'}))

    class Meta:
        model = SubjectChoice
        fields = "__all__"
        exclude=['serial','student']
 
    
        