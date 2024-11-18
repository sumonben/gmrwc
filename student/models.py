from django.db import models
import datetime
from django.template.defaultfilters import escape
from django.db import models
from django.urls import include, re_path, reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import format_html
from department.models import Department,Class,Session,Subject,Group
# Create your models here.
UserModel=get_user_model()


def year_choices():
    return [(r,r) for r in range(2009, datetime.date.today().year+1)]


    
class StudentCategory(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
class Division(models.Model):
    name=models.CharField(max_length=25,unique=True)
    name_en=models.CharField(max_length=15,unique=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name_en

class District(models.Model):
    name=models.CharField(max_length=25,unique=True)
    name_en=models.CharField(max_length=25,unique=True)
    lattitude=models.CharField(max_length=15,blank=True,null=True)
    longitude=models.CharField(max_length=15, blank=True,null=True)
    division=models.ForeignKey(Division, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name_en

class Upazilla(models.Model):
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    district=models.ForeignKey(District, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name_en

class Union(models.Model):
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    upazilla=models.ForeignKey(Upazilla, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)

    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name_en

class GuardianInfo(models.Model):
    serial=models.IntegerField(default=10)
    father_name=models.CharField(max_length=100,blank=True,null=True)
    father_name_en=models.CharField(max_length=100,blank=True,null=True)
    profession_of_father=models.CharField(max_length=25,blank=True,null=True)
    father_nid=models.CharField(max_length=25,blank=True,null=True)
    mother_name=models.CharField(max_length=100,blank=True,null=True)
    mother_name_en=models.CharField(max_length=100,blank=True,null=True)
    profession_of_mother=models.CharField(max_length=25,blank=True,null=True)
    mother_nid=models.CharField(max_length=100,blank=True,null=True)
    guardian_phone=models.CharField(max_length=11,blank=True,null=True)
    anual_income=models.CharField(max_length=11,blank=True,null=True)
    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.father_name:
            return self.father_name
        else:
            return '1'
    
class Adress(models.Model):
    serial=models.IntegerField(default=10)
    village_or_house=models.CharField(max_length=50,blank=True,null=True)
    house_or_street_no=models.CharField(max_length=25,blank=True,null=True)
    post_office=models.CharField(max_length=25,blank=True,null=True)
    division=models.ForeignKey(Division,blank=True,null=True,on_delete=models.SET_NULL)
    district=models.ForeignKey(District,blank=True,null=True,on_delete=models.SET_NULL)
    upazilla=models.ForeignKey(Upazilla,blank=True,null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.village_or_house:
            return self.village_or_house
        else:
            return '1'
            
class Student(models.Model):
    std_id=models.IntegerField(default=10)
    name=models.CharField(max_length=100)
    name_bangla=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=11,unique=True)
    class_roll=models.CharField(max_length=11,null=True, blank=True,)
    session=models.ForeignKey(Session,blank=True,null=True,on_delete=models.SET_NULL)
    student_category=models.ForeignKey(StudentCategory,blank=True,null=True,on_delete=models.SET_NULL)
    group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)
    section=models.CharField(max_length=25,null=True, blank=True,)
    department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    exam_roll=models.CharField(max_length=25,null=True, blank=True,)
    registration=models.CharField(max_length=25,null=True, blank=True,)
    class_year=models.ForeignKey(Class,blank=True,null=True,on_delete=models.SET_NULL)
    cgpa=models.CharField(max_length=15,null=True, blank=True,)
    date_of_birth=models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=15,null=True, blank=True,)
    passing_year=models.CharField( max_length=25, blank=True,null=True)
    nationality=models.CharField(max_length=15,null=True, blank=True,)
    birth_registration=models.CharField(max_length=25,null=True, blank=True,)
    religion=models.CharField(max_length=15,null=True, blank=True,)
    blood_group=models.CharField(max_length=10,null=True, blank=True,)
    marital_status=models.CharField(max_length=25,null=True, blank=True,)
    guardian_info=models.ForeignKey(GuardianInfo,on_delete=models.SET_NULL,null=True, blank=True,)
    present_adress=models.ForeignKey(Adress,null=True, blank=True,related_name="present_adress",on_delete=models.SET_NULL)
    permanent_adress=models.ForeignKey(Adress,null=True, blank=True,related_name="permanent_adress",on_delete=models.SET_NULL)
    image=models.ImageField(upload_to='media/',blank=True,null=True) 
    signature=models.ImageField(upload_to='media/',blank=True,null=True)
    user=models.OneToOneField(UserModel,blank=True,null=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)

    def user_link(self):
        if self.user is not None:
            return format_html('<a href="%s">%s</a>' % (reverse("admin:auth_user_change", args=(self.user.id,)) , escape(self.user.username)))
        else:
            return None
    user_link.allow_tags = True
    user_link.short_description = "User"
    
    def __str__(self):
        return self.name +':'+ self.phone
    
    def __unicode__(self):
        return self.name_bangla
    
    
class SscEquvalent(models.Model):
    serial=models.IntegerField(default=10)
    student=models.ForeignKey(Student,blank=True,null=True,on_delete=models.CASCADE)
    ssc_or_equvalent=models.CharField(max_length=25,blank=True,null=True)
    ssc_board=models.CharField(max_length=25,blank=True,null=True)
    ssc_group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)
    ssc_session=models.ForeignKey(Session,blank=True,null=True,on_delete=models.SET_NULL)
    ssc_exam_roll=models.CharField(max_length=25,blank=True,null=True)
    ssc_regitration_no=models.CharField(max_length=25,blank=True,null=True)
    ssc_cgpa_with_4th=models.CharField(max_length=25,blank=True,null=True)
    ssc_cgpa_without_4th=models.CharField(max_length=25,blank=True,null=True)
    ssc_passing_year=models.CharField( max_length=25, blank=True,null=True)
    
    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.student:
            return self.student.name+': '+self.student.phone
        return '1'
    
class SubjectChoice(models.Model):
    serial=models.IntegerField(default=10)
    student=models.ForeignKey(Student,blank=True,null=True,on_delete=models.CASCADE)
    compulsory_subject=models.ManyToManyField(Subject,related_name='compulsory_subject',blank=True,null=True)
    optional_subject=models.ManyToManyField(Subject,related_name='optional_subject',blank=True,null=True)
    fourth_subject=models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)

    
    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.student is not None:
            return self.student.name+': '+self.student.phone
        return '1'
    


class Transaction(models.Model):
    serial=models.IntegerField(default=10)
    student=models.ForeignKey(Student,blank=True,null=True,on_delete=models.CASCADE)
    phone=phone=models.CharField(max_length=11,unique=True,blank=True,null=True,)
    email=models.EmailField(max_length=50,blank=True,null=True)
    transactionID=models.CharField(max_length=25,blank=True,null=True)
    purpose=models.CharField(max_length=25,blank=True,null=True)
    method=models.CharField(max_length=100,blank=True,null=True)
    amount=models.CharField(max_length=25,blank=True,null=True)
    date=models.DateField(blank=True, null=True)
    refunded=models.BooleanField(default=False)
    
    class Meta:
        ordering = ['serial']
        unique_together = (('student', 'transactionID'),)
    def __str__(self):
        if self.student:
            return self.student
        else:
            return '1'


class StudentAdmission(models.Model):
    serial=models.IntegerField(default=10)
    ssc_roll=models.CharField(max_length=25,blank=True,null=True)
    name=models.CharField(max_length=125,blank=True,null=True)
    passing_year=models.CharField( max_length=25, blank=True,null=True)
    board=models.CharField(max_length=25,blank=True,null=True)
    group=models.CharField(max_length=25,blank=True,null=True)
    quota=models.CharField(max_length=25,blank=True,null=True)
    status=models.CharField(max_length=100,default="Not Admitted")

    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.ssc_roll
    def save(self, *args, **kwargs):
           super().save(*args, **kwargs)
           if self.serial == None:
                self.serial = self.id
                super().save()
    
