from django.db import models
from frontpage.models import Department,Category

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
SESSION_CHOICES = ( 
    ("1","2022-23" ), 
    ("2","2023-24"), 
    ("3","2024-25"), 
    ("4","2025-26"), 
    ("5","2026-27", ), 
    ("6","2027-28 "), 
    ("7","2028-29"), 
    ("8","2029-30"), 
) 

STUDENT_CATEGORY_CHOICES = ( 
    ("1","এইচএসসি" ), 
    ("2","অনার্স"), 
    ("3","মাস্টার্স"), 
) 
CLASS_YEAR_CHOICES = ( 
    ("1","১ম বর্ষ" ), 
    ("2","২য় বর্ষ"), 
    ("3","৩য় বর্ষ"), 
    ("4","৪র্থ বর্ষ"),
    ("5","১ম পর্ব"),
    ("6","শেষ পর্ব"),
    ("7","পাশকৃত"),   
   
      

)
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=11)
    class_roll=models.CharField(max_length=11)
    session=models.CharField(max_length=100,choices = SESSION_CHOICES, default = '4')
    student_category=models.CharField(max_length=100,choices = STUDENT_CATEGORY_CHOICES, default = '1')
    department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    exam_roll=models.CharField(max_length=25,null=True, blank=True,)
    registration=models.CharField(max_length=25,null=True, blank=True,)
    class_year=models.CharField(max_length=100, choices =CLASS_YEAR_CHOICES, default = '1')
    passing_year=models.DateField(blank=True, null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True) 
    signature=models.ImageField(upload_to='media/',blank=True,null=True)
    