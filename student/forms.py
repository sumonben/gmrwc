import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# import GeeksModel from models.py
from teacher.models import Teacher
from .models import Student,SubjectChoice,Upazilla,District,Division,Adress,SscEquvalent,Group,Session
from department.models import Department
 
# create a ModelForm

def year_choices():
    return [(r,r) for r in range(2009, datetime.date.today().year+1)]
BOARD_CHOICE=[
        ('Dhaka', 'Dhaka'),
        ('Rajshahi', 'Rajshahi'),
        ('Cattogram', 'Cattogram'),
        ('Khulna', 'Khulna'),
        ('Borishal', 'Borishal'),
        ('Dinajpur', 'Dinajpur'),
        ('Jassore', 'Jassore'),
        ('Maymansing', 'Maymansing'),
        ('Kumilla', 'Kumilla'),
        ('Madrasah', 'Madrasah'),
        ('Technical', 'Technical'),
        ('Vocationnal', 'Vocationnal'),

]
DEGREE_CHOICE=[
        ('SSC', 'SSC'),
        ('Dakhil', 'Dakhil'),
        ('Technical', 'Technical'),

]

class StudentForm(forms.ModelForm):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),

    ]
    gender= forms.ChoiceField(widget=forms.RadioSelect(),choices=CHOICES, )


    class Meta:
        MARITAL_CHOICES = [('Unmarried', 'Unmarried'),('Married', 'Married'),('Divorsed','Divorsed')]
        BlOOD_CHOICE=[('AB+', 'AB+'),('A+', 'A+'),('B+', 'B+'),('O+', 'O+'),('AB-', 'AB-'),('A-', 'A-'),('B-', 'B-'),('O-', 'O-'),]
        model = Student
        fields = "__all__"
        exclude=['std_id']
        department=forms.ModelChoiceField(label="",queryset=Department.objects.all(),empty_label="Placeholder",)

        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Name in English','onkeypress' : "myFunction(this.id);"}),
            'name_bangla': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'নাম লিখুন(বাংলায়)','onkeypress' : "myFunction(this.id);"}),
            'email': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Email','onkeypress' : "myFunction(this.id);"}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '11 digits ','onkeypress' : "myFunction(this.id);"}),
            'class_roll': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'ক্লাস রোল'}),
            'exam_roll': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'এক্সাম রোল (যদি থাকে)'}),
            'registration': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'রেজিস্ট্রেশন নম্বর(যদি থাকে)'}),
            'session': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;','onchange' : "myFunction(this.id);"}),
            'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
            'passing_year': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'student_category': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;','onchange' : "myFunction(this.id);"}),
            'group': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;'}),
            'birth_registration': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Birth registration Number'}),
            'nationality': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'nationality'}),
            'blood_group': forms.Select(choices=BlOOD_CHOICE,attrs={'class': 'textfieldUSER', 'placeholder':  'Your blood group'}),
            'marital_status': forms.Select(choices=MARITAL_CHOICES,attrs={'class': 'textfieldUSER',}),

            'department': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'class_year': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;','onchange' : "myFunction(this.id);"}),
      }
    
class SubjectChoiceForm(forms.ModelForm):
    compulsory_subject=forms.ModelMultipleChoiceField(Department.objects.all(),initial=Department.objects.filter(serial__in=[ 1, 2,3]), widget=FilteredSelectMultiple('Compulsory Subject',False, attrs={'row':'2'}))
    #optional_subject=forms.ModelMultipleChoiceField(Department.objects.all(), widget=FilteredSelectMultiple('Optional Subject',False, attrs={'row':'1','class': 'textfieldUSER',}))
    
    class Meta:
        model = SubjectChoice
        fields = "__all__"
        exclude=['serial','student','optional_subject']
        
class AdressForm(forms.ModelForm):
    division= forms.ModelChoiceField(queryset=Division.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSER'})),
    district=forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSER'})),
    upazilla= forms.ModelChoiceField(queryset=Upazilla.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSER'})),
            
    class Meta:
        model = Adress
        fields = "__all__"
        exclude=['serial']

        
        widgets = {
            'village_or_house': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Village Name/house No.','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'house_or_street_no': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Street Name/No.','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'post_office': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Bogura-5800','onkeypress' : "myFunction(this.id);"}),
            'division': forms.Select(attrs={'class': 'textfieldUSER',}),
            'district': forms.Select(attrs={'class': 'textfieldUSER',}),            
            'upazilla': forms.Select(attrs={'class': 'textfieldUSER',}),



        }
    
class SscEquvalentForm(forms.ModelForm):
    
    group= forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSER'}))
    session=forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSER'}))

    class Meta:
        model = SscEquvalent
        fields = "__all__"
        exclude=['serial','student']

        
        widgets = {
            'ssc_or_equvalent': forms.Select(choices=DEGREE_CHOICE,attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);"}),
            'board': forms.Select(choices=BOARD_CHOICE,attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id)"}),
            'group': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id)"}),
            'session': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id)"}),
            'exam_roll': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'SSC/Equivalent Roll'}),
            'regitration_no': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'SSC//Equivalent Registration'}),
            'cgpa_with_4th': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CGPA with 4th Subject'}),
            'cgpa_without_4th': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CGPA without 4th Subject','style': 'width: 100%;'}),
            'passing_year': forms.Select(choices=year_choices,attrs={'class': 'form-control', 'style': 'width: 100%; margin-bottom:3px;','onchange' : "myFunction(this.id);"}),
            }
