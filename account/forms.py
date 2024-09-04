
# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import Student
from department.models import Department
 
# create a ModelForm
class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = "__all__"
        exclude=['std_id']
        department=forms.ModelChoiceField(label="",queryset=Department.objects.all(),empty_label="Placeholder",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'নাম লিখুন'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ইমেইল'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ফোন নাম্বার'}),
            'class_roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ক্লাস রোল'}),
            'exam_roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'এক্সাম রোল'}),
            'registration': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'রেজিস্ট্রেশন নম্বর'}),
            'session': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'passing_year': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'student_category': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;'}),
            'department': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;','Placeholder':  'ফোন নাম্বার'}),
            'class_year': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
      }