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
DESIGNATION_CHOICES = ( 
    ("0","---পদবী---" ), 
    ("অধ্যাপক","অধ্যাপক" ), 
    ("সহযোগী অধ্যাপক","সহযোগী অধ্যাপক"), 
    ("সহকারী অধ্যাপক","সহকারী অধ্যাপক"), 
    ("প্রভাষক","প্রভাষক"), 
    ("প্রদর্শক","প্রদর্শক", ), 
    ("শরীরচর্চা শিক্ষক","শরীরচর্চা শিক্ষক"), 
    ("শিক্ষক","শিক্ষক"), 
    ("রদর্শক(অনিয়মিত)","প্রদর্শক(অনিয়মিত)"), 
) 
POSITION_CHOICES = ( 
    ("অধ্যক্ষ","অধ্যক্ষ" ), 
    ("উপাধ্যক্ষ","উপাধ্যক্ষ"),
    ("সম্পাদক (শিক্ষক পরিষদ)","সম্পাদক (শিক্ষক পরিষদ)"), 
    ("বিভাগীয় প্রধান","বিভাগীয় প্রধান"),
    ("শিক্ষক","শিক্ষক"),
    ("কর্মকর্তা","কর্মকর্তা"),
    ("অন্যান্য","অন্যান্য"), 
     

    

) 
BCS_BATCH=(
    ("0", "---বিসিএস ব্যাচ---"),("1", "প্রযোজ্য নয়"),("14", "14"), ("15", "15"),
     ("16", "16"), ("17", "17"), ("18", "18"), ("19", "19"), ("20", "20"), ("21", "21"), ("22", "22"),
      ("23", "23"), ("24", "24"),  ("25", "25"), ("26", "26"), ("27", "27"), ("28", "28"),("29", "29"), ("30", "30"),
     ("31", "31"), ("32", "32"),("33", "33"), ("34", "34"),  ("35", "35"), ("36", "66"), ("37", "37"), ("38", "38"),("39", "39"), ("40", "40"), 
    ("41", "41"), ("42", "42"),("43", "43"), ("44", "44"),  ("45", "45"), ("46", "46"), ("47", "47"), ("48", "48"),("49", "49"), ("50", "50"),
)



SESSION_CHOICES = ( 
    ("0","ভর্তি সেশন" ), 
    ("2022-23","2022-23" ), 
    ("2023-24","2023-24"), 
    ("2024-25","2024-25"), 
    ("2025-26","2025-26"), 
    ("2026-27","2026-27" ), 
    ("2027-28","2027-28"), 
    ("2028-29","2028-29"), 
    ("2029-30","2029-30"), 
) 

STUDENT_CATEGORY_CHOICES = ( 
    ("এইচএসসি","এইচএসসি" ), 
    ("অনার্স","অনার্স"), 
    ("মাস্টার্স","মাস্টার্স"), 
) 
GROUP_CHOICES = ( 
    ("বিজ্ঞান","বিজ্ঞান" ), 
    ("মানবিক","মানবিক"), 
    ("যবসা শিক্ষা","ব্যবসা শিক্ষা"), 
) 
CLASS_YEAR_CHOICES = ( 
    ("একাদশ","একাদশ" ), 
    ("দ্বাদশ","দ্বাদশ" ), 
    ("১ম বর্ষ","১ম বর্ষ" ), 
    ("২য় বর্ষ","২য় বর্ষ"), 
    ("৩য় বর্ষ","৩য় বর্ষ"), 
    ("৪র্থ বর্ষ","৪র্থ বর্ষ"),
    ("১ম পর্ব","১ম পর্ব"),
    ("শেষ পর্ব","শেষ পর্ব"),
    ("পাশকৃত","পাশকৃত"),   
   

)

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
