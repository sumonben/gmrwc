from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Department(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,unique=True)
    name_en=models.CharField(max_length=100,null=True,blank=True)
    code=models.CharField(max_length=20, null=True,blank=True)
    professor=models.IntegerField(default=0)
    associate_professor=models.IntegerField(default=0)
    assistant_professor=models.IntegerField(default=0)
    lecturer=models.IntegerField(default=0)
    demonstrator=models.IntegerField(default=0)



    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.name


class Branch(models.Model):
    serial=models.IntegerField(default=10)
    code=models.CharField(max_length=20, null=True,blank=True)
    name=models.CharField(max_length=100,unique=True)
    name_en=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        ordering = ['serial']
    
    def __str__(self):
        return self.name
