import datetime
from django.template.defaultfilters import escape
from django.db import models
from django.urls import include, re_path, reverse
from .manager import UserManager
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


'''class CustomUser(AbstractUser):
    username=None
    first_name=None
    last_name=None
    email=models.EmailField(max_length=100, unique=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20, unique=True)
    user_type= models.CharField(max_length=30, blank=True, null=True)
    email_is_verified=models.BooleanField(default=False,null=True)

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','phone']
    objects=UserManager()'''
