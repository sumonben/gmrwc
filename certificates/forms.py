import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# import GeeksModel from models.py
from teacher.models import Teacher
from department.models import Department,Subject,Session,Group,Class
from .models import Certificate
from student.models import StudentCategory
from student.forms import year_choices
from django.db.models import Q,Count

CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),

    ]

CHOICE_CERTIFICATE=[
        ('1', 'প্রশংসা পত্র'),
        ('2','চরিত্রগত সনদ'),
        ('3', 'ছাড়পত্র'),
        ('4', 'অধ্যয়নরত প্রত্যয়নপত্র'),
    

]

class ChoiceCertificateForm(forms.ModelForm):
    student_category= forms.ModelChoiceField(queryset=StudentCategory.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    choice_certificate= forms.ChoiceField(choices=CHOICE_CERTIFICATE,widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    group= forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))

    class Meta:
        model = Certificate
        fields = []

class CertificateForm(forms.ModelForm):
    gender= forms.CharField(
        widget=forms.RadioSelect(choices=CHOICES,),
         
    )
    session=forms.ModelChoiceField(queryset=Session.objects.all(),initial=Session.objects.last(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    passing_year= forms.ChoiceField(choices=year_choices,widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
    department= forms.ModelChoiceField(queryset=Department.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))

    class Meta:
        model = Certificate
        fields = "__all__"
        exclude=['student_category','adress','is_valid','subjects','transaction']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)",'value':'sumon'}),
            'name_bangla': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'নাম লিখুন(বাংলায়)','onkeypress' : "myFunction(this.id)",'value':'sumon'}),
            'father_name': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)",'value':'sumon'}),
            'father_name_bangla': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)",'value':'sumon'}),
            'mother_name': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)",'value':'sumon'}),
            'mother_name_bangla': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)",'value':'sumon'}),
            'email': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Email','onkeypress' : "myFunction(this.id)",'value':'sumo@gmail.com'}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  '11 digits ','onkeypress' : "myFunction(this.id)",'value':'01712534564'}),
            'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'textfieldUSERinfo', 'placeholder': 'Select a date','type': 'date'}),
            'group': forms.Select(attrs={'class': 'textfieldUSERinfo', 'style': 'margin-bottom:3px;','onchange' : "studentGroup(this.id)"}),
            'class_year': forms.Select(attrs={'class': 'textfieldUSERinfo', 'style': 'margin-bottom:3px;','onchange' : "studentGroup(this.id)"}),
            'birth_registration': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Birth registration Number'}),
            'nationality': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'nationality'}),
            
      }
