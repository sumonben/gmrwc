from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Department(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,unique=True)
    code=models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return self.name


class Branch(models.Model):
    serial=models.IntegerField(default=10)
    code=models.CharField(max_length=20, null=True,blank=True)
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name
