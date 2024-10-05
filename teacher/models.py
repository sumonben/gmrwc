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
from django.utils.html import format_html
# Create your models here.

UserModel=get_user_model()

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
class BcsBatch(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title

class Teacher(models.Model):
    tid=models.IntegerField(default=10, verbose_name="পদক্রম")
    t_name=models.CharField(max_length=100, verbose_name="নাম(ইংরেজি)")
    t_name_bangla=models.CharField(max_length=100,blank=True, null=True,verbose_name="নাম (বাংলা)")
    t_email=models.EmailField(max_length=50,unique=True,verbose_name="ই-মেইল")
    t_phone=models.CharField(max_length=11,unique=True,verbose_name="মোবাইল নং")
    designation=models.ForeignKey(Designation,blank=True,null=True,on_delete=models.CASCADE,verbose_name="পদবী")
    position=models.ManyToManyField(Position, null=True, blank=True, verbose_name="পদ")
    service_id=models.CharField(max_length=25 ,verbose_name="সার্ভিস আইডি")
    batch=models.ForeignKey(BcsBatch,blank=True,null=True,on_delete=models.CASCADE,verbose_name="বিসিএস ব্যাচ")
    merit=models.CharField(max_length=25,blank=True, null=True,verbose_name="মেরিট পজিশন")
    t_department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE,verbose_name="বিভাগ")
    branch=models.ManyToManyField(Branch, null=True, blank=True,verbose_name="শাখা")
    t_date_of_birth=models.DateField(blank=True, null=True, verbose_name="জন্ম তারিখ")
    first_joining_date=models.DateField(blank=True, null=True,verbose_name="প্রথম যোগদানের তারিখ")
    joining_date=models.DateField(blank=True, null=True,verbose_name="যোগদানের তারিখ")
    release_date=models.DateField(blank=True, null=True,verbose_name="রিলিজের তারিখ")
    image=models.ImageField(upload_to='media/',blank=True,null=True,verbose_name="ছবি") 
    signature=models.ImageField(upload_to='media/',blank=True,null=True,verbose_name="স্বাক্ষর")
    message=RichTextField(blank=True,null=True,verbose_name="মেসেজ(বাংলা)")
    message_en=RichTextField(blank=True,null=True,verbose_name="মেসেজ ইংরেজি")
    bio=RichTextField(blank=True,null=True,verbose_name="জীবনী (বাংলা)")
    bio_en=RichTextField(blank=True,null=True,verbose_name="জীবনী ইংরেজি")
    user=models.OneToOneField(UserModel,blank=True,null=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False, verbose_name="সক্রিয় কিনা?")
    class Meta:
        ordering = ['tid']
        
    def __str__(self):
        return self.t_name
    
    def __unicode__(self):
        return self.t_name_bangla

