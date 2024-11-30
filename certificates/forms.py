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
        ('', '----------'),
        ('1', 'প্রশংসা পত্র'),
        ('2','চরিত্রগত সনদ'),
        ('3', 'ছাড়পত্র'),
        ('4', 'অধ্যয়নরত প্রত্যয়নপত্র'),
    

]

class ChoiceCertificateForm(forms.ModelForm):
    student_category= forms.ModelChoiceField(queryset=StudentCategory.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    certificate_type= forms.ChoiceField(required=True,choices=CHOICE_CERTIFICATE,widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))
    group= forms.ModelChoiceField(required=False,queryset=Group.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','style':'display:none;',}))

    class Meta:
        model = Certificate
        fields = []

class CertificateForm(forms.ModelForm):
    gender= forms.CharField(
        widget=forms.RadioSelect(choices=CHOICES,),
         
    )
    def __init__(self,*args,**kwargs):
        category = kwargs.pop('student_category')
        type = kwargs.pop('certificate_type')

        super(CertificateForm,self).__init__(*args,**kwargs)
        self.fields['student_category']=forms.ModelChoiceField(queryset=StudentCategory.objects.all(),initial=StudentCategory.objects.filter(id=category).first(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))
        self.fields['certificate_type']=forms.ChoiceField(choices=CHOICE_CERTIFICATE,initial=type,widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))

        if category=="3" or category=="4":
                self.fields['session']=forms.ModelChoiceField(queryset=Session.objects.all(),initial=Session.objects.last(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
                self.fields['passing_year']= forms.ChoiceField(choices=year_choices,widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
                self.fields['department']=forms.ModelChoiceField(queryset=Department.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','style' : 'display:none',}),required=False)
                if category=="3":
                    self.fields['group']=forms.ModelChoiceField(queryset=Group.objects.filter(Q(id=1)|Q(id=2)|Q(id=3)),initial=Group.objects.last(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
                else:
                    self.fields['group']=forms.ModelChoiceField(queryset=Group.objects.filter(Q(id=4)|Q(id=5)|Q(id=6)|Q(id=7)|Q(id=8)|Q(id=9)),initial=Group.objects.last(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
        else:
                self.fields['session']=forms.ModelChoiceField(queryset=Session.objects.all(),initial=Session.objects.last(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
                self.fields['passing_year']= forms.ChoiceField(choices=year_choices,widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
                self.fields['department']=forms.ModelChoiceField(queryset=Department.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
                self.fields['group']=forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','style' : 'display:none',}),required=False)
          
    class Meta:
        model = Certificate
        fields = "__all__"
        exclude=['adress','is_valid','subjects','transaction','session_key','user']
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
            'class_year': forms.Select(attrs={'class': 'textfieldUSERinfo', 'style': 'margin-bottom:3px;','onchange' : "studentGroup(this.id)"}),
            'birth_registration': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Birth registration Number'}),
            'nationality': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'nationality'}),
            
      }

    
    

   