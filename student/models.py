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


def year_choices():
    return [(r,r) for r in range(2009, datetime.date.today().year+1)]

class Session(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
    
    
class Class(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
    
class Group(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
    
class StudentCategory(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title


class Student(models.Model):
    std_id=models.IntegerField(default=10)
    name=models.CharField(max_length=100)
    name_bangla=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=11,unique=True)
    class_roll=models.CharField(max_length=11,null=True, blank=True,)
    session=models.OneToOneField(Session,blank=True,null=True,on_delete=models.CASCADE)
    student_category=models.OneToOneField(StudentCategory,blank=True,null=True,on_delete=models.CASCADE)
    group=models.OneToOneField(Group,blank=True,null=True,on_delete=models.CASCADE)
    department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    exam_roll=models.CharField(max_length=25,null=True, blank=True,)
    registration=models.CharField(max_length=25,null=True, blank=True,)
    class_year=models.OneToOneField(Class,blank=True,null=True,on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True, null=True)
    passing_year=models.IntegerField( choices=year_choices, blank=True,null=True)
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
    def __unicode__(self):
        return self.name_bangla
