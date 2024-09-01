from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

TYPE_CHOICES=( ("1","static" ), 
    ("2","dynamic"),("3","link"),("4","department"))
DESIGNATION_CHOICES = ( 
    ("1","অধ্যাপক" ), 
    ("2","সহযোগী অধ্যাপক"), 
    ("3","সহকারী অধ্যাপক"), 
    ("4","প্রভাষক"), 
    ("5","প্রদর্শক", ), 
    ("6","শরীরচর্চা শিক্ষক"), 
    ("7","শিক্ষক"), 
    ("8","প্রদর্শক(অনিয়মিত)"), 
) 
POSITION_CHOICES = ( 
    ("1","অধ্যক্ষ" ), 
    ("2","উপাধ্যক্ষ"),
    ("3","সম্পাদক (শিক্ষক পরিষদ)"), 
    ("4","বিভাগীয় প্রধান"),
    ("5","শিক্ষক"),
    ("6","কর্মকর্তা"),
    ("7","অন্যান্য"), 
     

    

) 
BCS_BATCH=(
    ("0", "প্রযোজ্য নয়"),("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"), ("13", "13"), ("14", "14"), ("15", "15"),
     ("16", "16"), ("17", "17"), ("18", "18"), ("19", "19"), ("20", "20"), ("21", "21"), ("22", "22"),
      ("23", "23"), ("24", "24"),  ("25", "25"), ("26", "26"), ("27", "27"), ("28", "28"),("29", "29"), ("30", "30"),
     ("31", "31"), ("32", "32"),("33", "33"), ("34", "34"),  ("35", "35"), ("36", "66"), ("37", "37"), ("38", "38"),("39", "39"), ("40", "40"), 
    ("41", "41"), ("42", "42"),("43", "43"), ("44", "44"),  ("45", "45"), ("46", "46"), ("47", "47"), ("48", "48"),("49", "49"), ("50", "50"),
)
# Create your models here.
class Carousel(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=200)
    ctext=RichTextField(blank=True,null=True)
    cimage=models.ImageField(upload_to='media/',blank=True,null=True)

class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    code=models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return self.name


class Branch(models.Model):
    code=models.CharField(max_length=20, null=True,blank=True)
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    tid=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=11)
    designation=models.CharField(max_length=100,choices = DESIGNATION_CHOICES, default = '4')
    position=models.CharField(max_length=100,choices = POSITION_CHOICES, default = '1')
    service_id=models.CharField(max_length=25)
    batch=models.CharField(max_length=25,choices = BCS_BATCH, default = '0')
    merit=models.CharField(max_length=25,blank=True, null=True)
    department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    branch=models.ManyToManyField(Branch, null=True, blank=True,)
    first_joining_date=models.DateField(blank=True, null=True)
    joining_date=models.DateField(blank=True, null=True)
    release_date=models.DateField(blank=True, null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True) 
    signature=models.ImageField(upload_to='media/',blank=True,null=True)
    message=RichTextField(blank=True,null=True)
    bio=RichTextField(blank=True,null=True)

class Notice(models.Model):
    title=models.CharField(max_length=1000)
    body=models.TextField(blank=True, null=True)
    date=models.DateField(blank=True, null=True)
    file=models.FileField(upload_to='media/',blank=True,null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    published=models.BooleanField(default=False)


class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name
class Template(models.Model):
    name=models.CharField(max_length=25)
    directory=models.CharField(max_length=25,blank=True,null=True)
    def __str__(self):
            return self.directory+'/'+self.name
      
class Page(models.Model):
    heading=models.CharField(max_length=100,blank=True,null=True)
    title=models.CharField(max_length=500,blank=True,null=True)
    body=RichTextUploadingField(blank=True,null=True)
    type=models.CharField(max_length=25,choices = TYPE_CHOICES, default = '1')
    template=models.ForeignKey(Template,blank=True,null=True,on_delete=models.CASCADE)
    link=models.CharField(max_length=500,blank=True,null=True)
    date=models.DateField(blank=True, null=True)
    category=models.ManyToManyField(Category,blank=True,null=True,)
    tag=models.ManyToManyField(Tag,blank=True,null=True,)
    published=models.BooleanField(default=False)
    def __str__(self):
        return self.heading
class Post(models.Model):
    heading=models.CharField(max_length=100,blank=True,null=True)
    title=models.CharField(max_length=500)
    body=RichTextField(blank=True,null=True)
    file=models.FileField(upload_to='media/',blank=True,null=True)
    date=models.DateField(blank=True, null=True)
    category=models.ManyToManyField(Category,blank=True,null=True,)
    tag=models.ManyToManyField(Tag,blank=True,null=True,)
    published=models.BooleanField(default=False)
    def __str__(self):
        return self.title

class NavElement(models.Model):
    head=models.CharField(max_length=100,unique=True)
    page=models.ManyToManyField(Page, null=True, blank=True)
    def __str__(self):
        return self.head

class NavItem(models.Model):
    name=models.CharField(max_length=100,unique=True)
    navelement=models.ManyToManyField(NavElement, null=True,blank=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    def __str__(self):
        return self.name


class ServiceBox(models.Model):
    title=models.CharField(max_length=100,unique=True)
    element=models.ManyToManyField(Page, null=True, blank=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    def __str__(self):
        return self.title