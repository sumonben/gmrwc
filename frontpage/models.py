from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import escape
from django.urls import include, re_path, reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db import transaction
from django.db.models import F, Max

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
    serial=models.IntegerField(default=10)
    heading=models.CharField(max_length=100,blank=True,null=True)
    title=models.CharField(max_length=500,blank=True,null=True)
    body=RichTextUploadingField(blank=True,null=True)
    type=models.CharField(max_length=25,choices = TYPE_CHOICES, default = '1')
    template=models.ForeignKey(Template,blank=True,null=True,on_delete=models.CASCADE)
    link=models.CharField(max_length=500,blank=True,null=True)
    date=models.DateField(blank=True, null=True)
    category=models.ManyToManyField(Category,blank=True,null=True,)
    tag=models.ManyToManyField(Tag,blank=True,null=True,)
    '''rightsidebar_show=models.BooleanField(default=True)
    notice_show=models.BooleanField(default=True)
    carousel_show=models.BooleanField(default=True)
    plaiheader_show=models.BooleanField(default=True)
    topbar_show=models.BooleanField(default=True)
    published=models.BooleanField(default=False)'''
    


    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.heading
    def parent_nav_link(self):
        navelement=NavElement.objects.filter(page=self.id).first()
        navitem=None
        if navelement:
            navitem=NavItem.objects.filter(navelement=navelement.id).first()
        '''if navelement:
            str=format_html('<a href="%s">%s</a>'   % (reverse("admin:frontpage_navelement_change", args=(navelement.id)) , escape(navelement.head)))
        else:
            str=None'''
        if navitem:
            str=('<a href="%s">%s</a>'   % (reverse("admin:frontpage_navitem_change", args=([navitem.id])) , escape(navitem.name)))
            str2="-->"+('<a href="%s">%s</a>'   % (reverse("admin:frontpage_navelement_change", args=([navelement.id])) , escape(navelement.head)))
            strf=str+str2
            return format_html(strf)
        else:
            return navitem
class Post(models.Model):
    serial=models.IntegerField(default=10)
    heading=models.CharField(max_length=100,blank=True,null=True)
    title=models.CharField(max_length=500)
    body=RichTextField(blank=True,null=True)
    file=models.FileField(upload_to='media/',blank=True,null=True)
    date=models.DateField(blank=True, null=True)
    category=models.ManyToManyField(Category,blank=True,null=True,)
    tag=models.ManyToManyField(Tag,blank=True,null=True,)
    published=models.BooleanField(default=False)
    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title

class NavElement(models.Model):
    serial=models.IntegerField(default=10)
    head=models.CharField(max_length=100,unique=True)
    page=models.ManyToManyField(Page, null=True, blank=True)
    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.head
    def Related_pages(self):
        str="".join(format_html('<a href="%s">%s</a> || ' )  % (reverse("admin:frontpage_page_change", args=([p.id])) , escape(p.heading))for p in self.page.all())
        return format_html(str)
    
class NavItem(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,unique=True)
    navelement=models.ManyToManyField(NavElement, null=True,blank=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.name
    '''def save(self):
        with transaction.atomic():
            count = NavItem.objects.count()

            objects = NavItem.objects.all()
            if count > 100:
                objects[0].delete()
                if count > 1:
                    objects.update(id=F('id') - 1)

            if not self.id and count > 0:
                objects = objects.refresh_from_db()  # Update QuerySet
                self.id = objects.annotate(max_count=Max('id')).max_count + 1
            elif not self.id and count == 0:
                self.id = 1

            self.save()'''
            
    def Child_Element_link(self):
        nav=self.navelement.all()
        str=""
        for p in self.navelement.all():
            str=str+format_html('<a href="%s">%s</a></div><br>----------> ' )  % (reverse("admin:frontpage_navelement_change", args=([p.id])) , escape(p.head))
            for page in p.page.all():
                str=str+format_html('<a href="%s">%s</a> || ' )  % (reverse("admin:frontpage_page_change", args=([page.id])) , escape(page.heading))
            str=str+"<br><br>"

           # for page in p.page.all():
                #str=str.join(format_html('<a href="%s">%s</a> || ' )  % (reverse("admin:frontpage_page_change", args=([page.id])) , escape(page.heading)))
  
        #str="".join(format_html('<a href="%s">%s</a> || ' )  % (reverse("admin:frontpage_navelement_change", args=([p.id])) , escape(p.head))for p in self.navelement.all())
   
        #str=format_html('<a href="%s">%s</a> || ' )  % (reverse("admin:frontpage_navelement_change", args=([p.id])) , escape(p.head))+format_html('<a href="%s">%s</a> || ' )  % (reverse("admin:frontpage_page_change", args=([page.id])) , escape(page.heading))for page in p.page.all() for p in self.navelement.all()) 
        return format_html(str)
        #return format_html('<a href="%s">%s</a>' % (reverse("admin:frontpage_navelement_change", args=([self.id])) , escape([ self.navelement.all().first()])))



class ServiceBox(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    element=models.ManyToManyField(Page, null=True, blank=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
    def Related_pages(self):
        str="".join(format_html('<a href="%s">%s</a> || ' )  % (reverse("admin:frontpage_page_change", args=([p.id])) , escape(p.heading))for p in self.element.all())
        return format_html(str)