from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
TYPE_CHOICE={
    ('Compulsory','Compulsory'),
    ('Optional','Optional'),
    ('Major','Major'),
    ('Non-Major','Non-Major'),
}
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
    
'''class Subject(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,unique=True)
    name_en=models.CharField(max_length=100,null=True,blank=True)
    code=models.CharField(max_length=20, null=True,blank=True)
    group=models.ManyToManyField(Group, blank=True,null=True)
    department=models.ManyToManyField(Department, blank=True,null=True)
    type=models.Choices(choices=TYPE_CHOICE,blank=True,null=True)
    is_available=models.BooleanField(default=True)



    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.name_en'''
