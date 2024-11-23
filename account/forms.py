
# import form class from django
import datetime
from django import forms
 
# import GeeksModel from models.py
from teacher.models import Teacher
from student.models import Student, StudentCategory
from student.forms import year_choices
from department.models import Department,Session,Group,Class

year_choice=year_choices()
# create a ModelForm
class StudentForm(forms.ModelForm):
    # specify the name of model to use
    department=forms.ModelChoiceField(required=False,queryset=Department.objects.all(),empty_label="Department", widget=forms.Select(attrs={'class': 'form-control','onchange' : 'check_field_class_year()',}))
    group=forms.ModelChoiceField(required=False,queryset=Group.objects.all(),empty_label="Group", widget=forms.Select(attrs={'class': 'form-control',}))
    session=forms.ModelChoiceField(queryset=Session.objects.all(),empty_label="Session",widget=forms.Select(attrs={'class': 'form-control',}))
    class_year=forms.ModelChoiceField(queryset=Class.objects.all(),widget=forms.Select(attrs={'class': 'form-control',}))
    student_category=forms.ModelChoiceField(queryset=StudentCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control',}))
    passing_year=forms.ChoiceField(choices=year_choices(),widget=forms.Select(attrs={'class': 'form-control',}))

    class Meta:
        model = Student
        fields = "__all__"
        exclude=['std_id','class_roll','exam_roll','registration','section','cgpa','guardian_info','present_adress','permanent_adress','user','is_active',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'নাম লিখুন(ইংরেজিতে)','onkeypress' : "myFunction(this.id);"}),
            'name_bangla': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'নাম লিখুন(বাংলায়)','onkeypress' : "myFunction(this.id);"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ইমেইল','onkeypress' : "myFunction(this.id);"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ফোন নাম্বার','onkeypress' : "myFunction(this.id);"}),
            'class_roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ক্লাস রোল'}),
            'exam_roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'এক্সাম রোল (যদি থাকে)'}),
            'registration': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'রেজিস্ট্রেশন নম্বর(যদি থাকে)'}),
            'session': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;','onchange' : "myFunction(this.id);"}),
            'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
            'student_category': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;','onchange' : "myFunction(this.id);"}),
            'group': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;'}),
            'department': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'class_year': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;','onchange' : "myFunction(this.id);"}),
      }
class TeacherForm(forms.ModelForm):
    # specify the name of model to use
    #department=forms.ModelChoiceField(label="",queryset=Department.objects.all(),empty_label="Placeholder",)
    class Meta:
        model = Teacher
        fields = "__all__"
        exclude=['tid']
        
        widgets = {
            't_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'নাম লিখুন(ইংরেজিতে)','onkeypress' : "myFunctionTeacher(this.id);"}),
            't_name_bangla': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'নাম লিখুন(বাংলায়)','onkeypress' : "myFunctionTeacher(this.id);"}),
            't_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ইমেইল','onkeypress' : "myFunctionTeacher(this.id);"}),
            't_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'ফোন নাম্বার','onkeypress' : "myFunctionTeacher(this.id);"}),
            'designation': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;','onchange' : "myFunctionTeacher(this.id);"}),
            'service_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'সার্ভিস আইডি( যদি থাকে)'}),
            't_department': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;','onchange' : "myFunctionTeacher(this.id);"}),
            'batch': forms.Select(attrs={'class': 'form-control','style': 'width: 100%;' }),
            'merit': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  ' মেরিট পজিশন(যদি থাকে)'}),
            't_date_of_birth': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
            'first_joining_date': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date','onchange' : "myFunctionTeacher(this.id);"}),
            'joining_date': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date','onchange' : "myFunctionTeacher(this.id);"}),
            'release_date': forms.DateInput(format=('%y-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
            'position': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;'}),
            'branch': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;'}),
            'class_year': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
      }