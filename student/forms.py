import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# import GeeksModel from models.py
from teacher.models import Teacher
from department.models import Department,Subject,Session,Group,Class
from .models import Student,SubjectChoice,Upazilla,District,Division,Adress,SscEquvalent,GuardianInfo
from department.models import Department
from django.db.models import Q,Count

# create a ModelForm
MARITAL_CHOICES = [('Unmarried', 'Unmarried'),('Married', 'Married'),('Divorced','Divorced')]
BlOOD_CHOICE=[('AB+', 'AB+'),('A+', 'A+'),('B+', 'B+'),('O+', 'O+'),('AB-', 'AB-'),('A-', 'A-'),('B-', 'B-'),('O-', 'O-'),]
        
def year_choices():
    return [(r,r) for r in range(2009, datetime.date.today().year+1)]
    
BOARD_CHOICE=[
        ('Dhaka', 'Dhaka'),
        ('Rajshahi', 'Rajshahi'),
        ('Chattogram', 'Chattogram'),
        ('Khulna', 'Khulna'),
        ('Barisal', 'Barisal'),
        ('Dinajpur', 'Dinajpur'),
        ('Jassore', 'Jassore'),
        ('Mymensing', 'Mymensing'),
        ('Sylhet', 'Sylhet'),
        ('Cumilla', 'Cumilla'),
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
        
class StudentForm(forms.ModelForm):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),

    ]
    gender= forms.CharField(
        widget=forms.RadioSelect(choices=CHOICES,),
         
    )
    session=forms.ModelChoiceField(queryset=Session.objects.all(),initial=Session.objects.last(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))


    class Meta:
        MARITAL_CHOICES = [('Unmarried', 'Unmarried'),('Married', 'Married'),('Divorced','Divorced')]
        BlOOD_CHOICE=[('AB+', 'AB+'),('A+', 'A+'),('B+', 'B+'),('O+', 'O+'),('AB-', 'AB-'),('A-', 'A-'),('B-', 'B-'),('O-', 'O-'),]
        model = Student
        fields = "__all__"
        exclude=['std_id','class_roll','exam_roll','registration','passing_year','student_category','department','section','class_year','cgpa','guardian_info','present_adress','permanent_adress','user','is_active','gender',]
        #department=forms.ModelChoiceField(label="",queryset=Department.objects.all(),empty_label="Placeholder",)

        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSERinfo',  'placeholder':  'Name in English','onkeypress' : "myFunction(this.id)"}),
            'name_bangla': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'নাম লিখুন(বাংলায়)','onkeypress' : "myFunction(this.id)"}),
            'email': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Email','onkeypress' : "myFunction(this.id)"}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  '11 digits ','onkeypress' : "myFunction(this.id)"}),
            'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'textfieldUSERinfo', 'placeholder': 'Select a date','type': 'date'}),
            'group': forms.Select(attrs={'class': 'textfieldUSERinfo', 'style': 'margin-bottom:3px;','onchange' : "studentGroup(this.id)"}),
            'birth_registration': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Birth registration Number'}),
            'nationality': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'nationality'}),
            'blood_group': forms.Select(choices=BlOOD_CHOICE,attrs={'class': 'textfieldUSERinfo', 'placeholder':  'Your blood group'}),
            'marital_status': forms.Select(choices=MARITAL_CHOICES,attrs={'class': 'textfieldUSERinfo',}),
            'religion': forms.Select(choices=RELIGION_CHOICES,attrs={'class': 'textfieldUSERinfo',}),
            

      }

class GuardianForm(forms.ModelForm):
    

    class Meta:
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
    #compulsory_subject=forms.ModelMultipleChoiceField(queryset=Subject.objects.all(),initial=Subject.objects.filter(serial__in=[ 1, 2,3]), widget=FilteredSelectMultiple('Subject',False, attrs={'class':'textfieldUSERinfo'}))
    
    #optional_subject=forms.ModelMultipleChoiceField(Subject.objects.all(), widget=FilteredSelectMultiple('Optional Subject',False, attrs={'row':'1','class': 'textfieldUSER',}))
    #group= forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))

    class Meta:
        model = SubjectChoice
        fields = "__all__"
        exclude=['serial','student',]
        widgets={
                        'fourth_subject': forms.Select(attrs={'class': 'textfieldUSERinfo','onclick' : "fourthSubject(this.id);",'style':'margin-bottom:20px'}),

        }
    class Media:
            css = {
                'all': ('/static/admin/css/widgets.css',),
            }
            js = ('/admin/jsi18n',)
        
    def clean_compulsory_subject(self):
            compulsory_subject = self.cleaned_data['compulsory_subject']
            return compulsory_subject
        
    def __init__(self,*args,**kwargs):
        
        group = kwargs.pop('group')
        super(SubjectChoiceForm,self).__init__(*args,**kwargs)
        if group:
            if group.title_en=="Science":
                self.fields['compulsory_subject']=forms.ModelMultipleChoiceField(queryset=Subject.objects.filter(Q(group=group)|Q(group=None)),initial=Subject.objects.filter(serial__in=[ 1, 2,3,4,5,]), widget=FilteredSelectMultiple('Comulsory Subject',True, attrs={'class':'textfieldUSERinfo',}))
                self.fields['optional_subject']=forms.ModelMultipleChoiceField(queryset=Subject.objects.filter(group=group, type='Fourth'), widget=FilteredSelectMultiple('Optional Subject',False, attrs={'class':'textfieldUSERinfo',}))
            if group.title_en=="Humanities":
                self.fields['compulsory_subject']=forms.ModelMultipleChoiceField(queryset=Subject.objects.filter(Q(group=group)|Q(group=None)),initial=Subject.objects.filter(serial__in=[ 1, 2,3,8]), widget=FilteredSelectMultiple('Comulsory Subject',True, attrs={'class':'textfieldUSERinfo',}))
                self.fields['optional_subject']=forms.ModelMultipleChoiceField(queryset=Subject.objects.filter(group=group, type='Optional'), widget=FilteredSelectMultiple('Optional Subject',False, attrs={'class':'textfieldUSERinfo',}))
                self.fields['fourth_subject']=forms.ModelChoiceField(queryset=Subject.objects.filter(group=group, type='Optional'), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
            if group.title_en=="Business Studies":
                self.fields['compulsory_subject']=forms.ModelMultipleChoiceField(queryset=Subject.objects.filter(Q(group=group)|Q(group=None)),initial=Subject.objects.filter(serial__in=[ 1, 2,3,13,14,16]), widget=FilteredSelectMultiple('Comulsory Subject',True, attrs={'class':'textfieldUSERinfo',}))
                self.fields['fourth_subject']=forms.ModelChoiceField(queryset=Subject.objects.filter(serial__in=[9,]),initial=Subject.objects.filter(serial__in=[ 9,]), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
                if 'optional_subject' in self.fields: del self.fields['optional_subject']
                #self.fields['compulsory_subject'].initial=Subject.objects.filter(serial__in=[ 1, 2,3])
                #self.fields['compulsory_subject'].widget = FilteredSelectMultiple('Subject',False, attrs={'class':'textfieldUSERinfo'})

            
        
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

'''class SscEquvalentForm(forms.Form):
    
    ssc_or_equvalent= forms.ChoiceField(choices=DEGREE_CHOICE,widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
    ssc_group=forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
    ssc_board= forms.ChoiceField(choices=BOARD_CHOICE,widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
    ssc_session=forms.ModelChoiceField(queryset=Session.objects.all(),widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))
    ssc_exam_roll= forms.CharField(widget=forms.TextInput(attrs={'class':'textfieldUSERinfo'}))
    ssc_regitration_no=forms.CharField(widget=forms.TextInput(attrs={'class':'textfieldUSERinfo'}))
    ssc_cgpa_with_4th= forms.CharField(widget=forms.TextInput(attrs={'class':'textfieldUSERinfo'}))
    ssc_cgpa_without_4th=forms.CharField(widget=forms.TextInput(attrs={'class':'textfieldUSERinfo'}))
    ssc_passing_year=forms.ChoiceField(choices=year_choices,widget=forms.Select(attrs={'class':'textfieldUSERinfo'}))'''
    
class SscEquvalentForm(forms.ModelForm):
    
    '''group=forms.ModelChoiceField(label="",queryset=Group.objects.all().values_list('id', 'title_en'),empty_label="Placeholder",)
    session=forms.ModelChoiceField(label="",queryset=Session.objects.all().values_list('id', 'title_en'),empty_label="Placeholder",)'''
    ssc_passing_year= forms.ChoiceField(choices=year_choices,widget=forms.Select(attrs={'class':'textfieldUSER'}))

    class Meta:
        model = SscEquvalent
        fields = "__all__"
        exclude=['serial','student']

        
        widgets = {
            'ssc_or_equvalent': forms.Select(choices=DEGREE_CHOICE,attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id);"}),
            'ssc_board': forms.Select(choices=BOARD_CHOICE,attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id)"}),
            'ssc_group': forms.Select(attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id);",'required':'true'}),
            'ssc_session': forms.Select(attrs={'class': 'textfieldUSERinfo','onkeypress' : "myFunction(this.id);",'required':'true'}),
            'ssc_exam_roll': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'SSC/Equivalent Roll'}),
            'ssc_regitration_no': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder':  'SSC/Equivalent Registration'}),
            'ssc_cgpa_with_4th': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder': 'CGPA with 4th Subject'}),
            'ssc_cgpa_without_4th': forms.TextInput(attrs={'class': 'textfieldUSERinfo', 'placeholder': 'CGPA without 4th Subject'}),
            }