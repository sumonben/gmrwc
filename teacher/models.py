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
        return self.id
class BcsBatch(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title

class Teacher(models.Model):
    tid=models.IntegerField(default=10)
    t_name=models.CharField(max_length=100)
    t_name_bangla=models.CharField(max_length=100,blank=True, null=True)
    t_email=models.EmailField(max_length=50,unique=True)
    t_phone=models.CharField(max_length=11,unique=True)
    designation=models.OneToOneField(Designation,blank=True,null=True,on_delete=models.CASCADE)
    position=models.ManyToManyField(Position, null=True, blank=True,)
    service_id=models.CharField(max_length=25)
    batch=models.OneToOneField(BcsBatch,blank=True,null=True,on_delete=models.CASCADE)
    merit=models.CharField(max_length=25,blank=True, null=True)
    t_department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    branch=models.ManyToManyField(Branch, null=True, blank=True,)
    t_date_of_birth=models.DateField(blank=True, null=True)
    first_joining_date=models.DateField(blank=True, null=True)
    joining_date=models.DateField(blank=True, null=True)
    release_date=models.DateField(blank=True, null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True) 
    signature=models.ImageField(upload_to='media/',blank=True,null=True)
    message=RichTextField(blank=True,null=True)
    message_en=RichTextField(blank=True,null=True)
    bio=RichTextField(blank=True,null=True)
    bio_en=RichTextField(blank=True,null=True)
    user=models.OneToOneField(UserModel,blank=True,null=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)
    class Meta:
        ordering = ['tid']
    def __unicode__(self):
        return self.t_name_bangla

