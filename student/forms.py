import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# import GeeksModel from models.py
from teacher.models import Teacher
from .models import Student,SubjectChoice,Upazilla,District,Division,Adress,SscEquvalent,Group,Session,GuardianInfo
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
RELIGION_CHOICES=[
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Christanity', 'Christanity'),
        ('Buddhism', 'Buddhism'),


]

class StudentForm(forms.ModelForm):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),

    ]
    gender= forms.ChoiceField(widget=forms.RadioSelect(),choices=CHOICES, )
    session=forms.ModelChoiceField(required=True,queryset=Session.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : "myFunction(this.id)",}))


    class Meta:
        MARITAL_CHOICES = [('Unmarried', 'Unmarried'),('Married', 'Married'),('Divorced','Divorced')]
        BlOOD_CHOICE=[('AB+', 'AB+'),('A+', 'A+'),('B+', 'B+'),('O+', 'O+'),('AB-', 'AB-'),('A-', 'A-'),('B-', 'B-'),('O-', 'O-'),]
        model = Student
        fields = "__all__"
        exclude=['std_id','class_roll','exam_roll','registration','passing_year','student_category','department','section','class_year','guardian_info','present_adress','permanent_adress','user','is_active','gender',]
        department=forms.ModelChoiceField(label="",queryset=Department.objects.all(),empty_label="Placeholder",)

        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)",}),
            'name_bangla': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'নাম লিখুন(বাংলায়)','onkeypress' : "myFunction(this.id)"}),
            'email': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Email','onkeypress' : "myFunction(this.id)"}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  '11 digits ','onkeypress' : "myFunction(this.id)"}),
            'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'textfieldUSERinfo', 'placeholder': 'Select a date','type': 'date'}),
            'group': forms.Select(attrs={'class': 'textfieldUSERinfo', 'style': 'margin-bottom:3px;'}),
            'birth_registration': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Birth registration Number'}),
            'nationality': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'nationality'}),
            'blood_group': forms.Select(choices=BlOOD_CHOICE,attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Your blood group'}),
            'marital_status': forms.Select(choices=MARITAL_CHOICES,attrs={'class': 'textfieldUSERinfo',}),
            'religion': forms.Select(choices=RELIGION_CHOICES,attrs={'class': 'textfieldUSERinfo',}),
            

      }
class GuardianForm(forms.ModelForm):
    

    class Meta:
        FATHER_PROFESSION_CHOICE = [
        ('Agriculture Farming', 'Agriculture Farming'),
        ('Business', 'Business'),
        ('Govt. Service', 'Govt. Service'),
        ('NonGovt. Service', 'NonGovt. Service'),

        ]
        MOTHER_PROFESSION_CHOICE = [
        ('House Wife', 'House Wife'),
        ('Business', 'Business'),
        ('Govt. Service', 'Govt. Service'),
        ('NonGovt. Service', 'NonGovt. Service'),

        ]
        model = GuardianInfo
        fields = "__all__"
        exclude=['serial',]

        
        widgets = {
            'father_name_en': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)"}),
            'father_name': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'নাম লিখুন(বাংলায়)','onkeypress' : "myFunction(this.id)"}),
            'profession_of_father': forms.Select(choices=FATHER_PROFESSION_CHOICE,attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Email','onkeypress' : "myFunction(this.id)"}),
            'father_nid': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  '11 digits ','onkeypress' : "myFunction(this.id)"}),
            'mother_name': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'নাম লিখুন(বাংলায়)','onchange' : "myFunction(this.id)"}),
            'mother_name_en': forms.TextInput(attrs={'class': 'textfieldUSERinfo','placeholder':  'Name in English'}),
            'profession_of_mother': forms.Select(choices=MOTHER_PROFESSION_CHOICE,attrs={'class': 'textfieldUSERinfo', 'style': 'margin-bottom:3px;','required':'true'}),
            'mother_nid': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Mother NID Number'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  '11 digits '}),
            'anual_income': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Anual Family Income'}),
           


      }
  
class SubjectChoiceForm(forms.ModelForm):
    compulsory_subject=forms.ModelMultipleChoiceField(Department.objects.all(),initial=Department.objects.filter(serial__in=[ 1, 2,3]), widget=FilteredSelectMultiple('Subject',False, attrs={'class':'textfieldUSERinfo'}))
    #optional_subject=forms.ModelMultipleChoiceField(Department.objects.all(), widget=FilteredSelectMultiple('Optional Subject',False, attrs={'row':'1','class': 'textfieldUSER',}))
    #group= forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))

    class Meta:
        model = SubjectChoice
        fields = "__all__"
        exclude=['serial','student','optional_subject']
        widgets={
                        'fourth_subject': forms.Select(attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id);",'style':'margin-bottom:20px'}),
                        'compulsory_subject': forms.SelectMultiple(attrs={'class': 'textfieldUSERinfo','style':'margin-top:20px','onkeypress' : "myFunction(this.id);"}),

        }
        
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
class PresentAdressForm(forms.ModelForm):
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
    
    group= forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
    session=forms.ModelChoiceField(queryset=Session.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))

    class Meta:
        model = SscEquvalent
        fields = "__all__"
        exclude=['serial','student']

        
        widgets = {
            'ssc_or_equvalent': forms.Select(choices=DEGREE_CHOICE,attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id);"}),
            'board': forms.Select(choices=BOARD_CHOICE,attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id)"}),
            'group': forms.Select(attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id);",'required':'true'}),
            'session': forms.Select(attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id);",'required':'true'}),
            'exam_roll': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'SSC/Equivalent Roll'}),
            'regitration_no': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'SSC/Equivalent Registration'}),
            'cgpa_with_4th': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder': 'CGPA with 4th Subject'}),
            'cgpa_without_4th': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder': 'CGPA without 4th Subject'}),
            'passing_year': forms.Select(choices=year_choices,attrs={'class': 'textfieldUSERinfo', 'style': 'margin-bottom:3px;','onchange' : "myFunction(this.id);"}),
            }
