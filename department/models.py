from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from frontpage.models import Category,Tag
# Create your models here.
TYPE_CHOICE={
    ('Compulsory','Compulsory'),
    ('Optional','Optional'),
    ('Fourth','Fourth'),
    ('Major','Major'),
    ('Non-Major','Non-Major'),
}
NAV_TYPE_CHOICES=( ("1","static" ), 
    ("2","dynamic"),("3","link"),("4","department"))


class Department(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,unique=True)
    name_en=models.CharField(max_length=100,null=True,blank=True,verbose_name="Name(In English)")
    code=models.CharField(max_length=20, null=True,blank=True)
    about=RichTextUploadingField(blank=True,null=True)
    about_en=RichTextUploadingField(blank=True,null=True,verbose_name="About(In English)")
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

class Session(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en
    
    
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
        return self.title_en

  
class Subject(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,unique=True)
    name_en=models.CharField(max_length=100,null=True,blank=True)
    code=models.CharField(max_length=20, null=True,blank=True)
    group=models.ManyToManyField(Group, blank=True,null=True)
    department=models.ManyToManyField(Department, blank=True,null=True)
    type=models.CharField(max_length=25,blank=True,null=True)
    is_available=models.BooleanField(default=True)



    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.name_en

class NavDepartmentElement(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)
    body=RichTextUploadingField(blank=True,null=True)
    body_en=RichTextUploadingField(blank=True,null=True)
    type=models.CharField(max_length=25,choices = NAV_TYPE_CHOICES, default = '1')
    link=models.CharField(max_length=500,blank=True,null=True)
    category=models.ManyToManyField(Category,blank=True,null=True,)
    tag=models.ManyToManyField(Tag,blank=True,null=True,)
    department=models.ManyToManyField(Department, blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title

class NavDepartment(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)
    element=models.ManyToManyField(NavDepartmentElement, null=True, blank=True)
    link=models.CharField(max_length=500,blank=True,null=True)
    department=models.ManyToManyField(Department, blank=True,null=True)


    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
    '''def Related_pages(self):
        str="".join(format_html('<a href="%s" target="_blank">%s</a> || ' )  % (reverse("admin:frontpage_page_change", args=([p.id])) , escape(p.heading))for p in self.element.all())
        return format_html(str)'''