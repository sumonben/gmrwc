from django.db import models
import datetime
from django.template.defaultfilters import escape
from django.db import models
from django.urls import include, re_path, reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from department.models import Department,Branch
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
UserModel=get_user_model()

DESIGNATION_CHOICES = ( 
    ("0","---পদবী---" ), 
    ("1","অফিস সহকারী" ), 
    ("2","কম্পিউটার অপারেটর"), 
    ("3","ড্রাইভার"), 
    ("4","অফিস সহায়ক"), 
    ("5","পরিছন্নতা কর্মী", ), 
    ("6",""), 
    
) 
POSITION_CHOICES = ( 
    ("1","অধ্যক্ষ" ), 
    ("2","উপাধ্যক্ষ"),
    ("3","সম্পাদক (শিক্ষক পরিষদ)"), 
    ("4","বিভাগীয় প্রধান"),
    ("5","শিক্ষক"),
    ("6","কর্মকর্তা"),
    ("অন্যান্য","অন্যান্য"), 
     

    

) 
EMLPLOYEE_TYPE=(
    ("1","নিয়মিত" ), 
    ("2","অনিয়মিত"),
)

class Designation(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title

class Position(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
class Type(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title

class Employee(models.Model):
    serial=models.IntegerField(default=10, verbose_name="পদক্রম")
    employee_name=models.CharField(max_length=100, verbose_name="নাম(ইংরেজি)")
    employee_name_bangla=models.CharField(max_length=100,blank=True, null=True,verbose_name="নাম (বাংলা)")
    employee_email=models.EmailField(max_length=50,unique=True,verbose_name="ই-মেইল")
    employee_phone=models.CharField(max_length=11,unique=True,verbose_name="মোবাইল নং")
    designation=models.ForeignKey(Designation, max_length=100, blank=True,null=True, on_delete=models.SET_NULL,verbose_name="পদবী")
    position=models.ForeignKey(Position,max_length=100, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="পদ")
    service_id=models.CharField(max_length=25 ,verbose_name="সার্ভিস আইডি")
    employee_department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL,verbose_name="বিভাগ")
    branch=models.ManyToManyField(Branch, null=True, blank=True,verbose_name="শাখা")
    employee_type=models.ForeignKey(Type, max_length=100,blank=True, on_delete=models.SET_NULL, null=True,verbose_name="কর্মচারীর ধরণ")
    date_of_birth=models.DateField(blank=True, null=True, verbose_name="জন্ম তারিখ")
    first_joining_date=models.DateField(blank=True, null=True,verbose_name="প্রথম যোগদানের তারিখ")
    joining_date=models.DateField(blank=True, null=True,verbose_name="যোগদানের তারিখ")
    release_date=models.DateField(blank=True, null=True,verbose_name="রিলিজের তারিখ")
    image=models.ImageField(upload_to='media/',blank=True,null=True,verbose_name="ছবি") 
    signature=models.ImageField(upload_to='media/',blank=True,null=True,verbose_name="স্বাক্ষর")
    bio=RichTextField(blank=True,null=True,verbose_name="জীবনী (বাংলা)")
    bio_en=RichTextField(blank=True,null=True,verbose_name="জীবনী ইংরেজি")
    user=models.OneToOneField(UserModel,blank=True,null=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False, verbose_name="সক্রিয় কিনা?")
    class Meta:
        ordering = ['serial']
        
    def __str__(self):
        return self.employee_name
    
    def __unicode__(self):
        return self.employee_name_bangla