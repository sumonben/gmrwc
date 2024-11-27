from django.db import models
from django.urls import reverse
from student.models import StudentCategory,Adress,SubjectChoice
from payment.models import Transaction
from department.models import Session,Department,Group,Class
from django.utils.html import format_html
from django.template.defaultfilters import escape
from account.models import UserModel
# Create your models here.
class Certificate(models.Model):
    name=models.CharField(max_length=100)
    name_bangla=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(max_length=50,null=True)
    phone=models.CharField(max_length=11,null=True)
    father_name=models.CharField(max_length=100)
    father_name_bangla=models.CharField(max_length=100,blank=True, null=True)
    mother_name=models.CharField(max_length=100)
    mother_name_bangla=models.CharField(max_length=100,blank=True, null=True)
    student_category=models.ForeignKey(StudentCategory,blank=True,null=True,on_delete=models.SET_NULL)
    session=models.ForeignKey(Session,blank=True,null=True,on_delete=models.SET_NULL)
    group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)
    department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    class_year=models.ForeignKey(Class,blank=True,null=True,on_delete=models.SET_NULL)
    section=models.CharField(max_length=25,null=True, blank=True,)
    class_roll=models.CharField(max_length=11,null=True, blank=True,)
    exam_roll=models.CharField(max_length=25,null=True, blank=True,)
    registration=models.CharField(max_length=25,null=True, blank=True,)
    cgpa=models.CharField(max_length=15,null=True, blank=True,)
    passing_year=models.CharField( max_length=25, blank=True,null=True)
    subjects=models.ForeignKey(SubjectChoice,null=True, blank=True,on_delete=models.SET_NULL)
    date_of_birth=models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=15,null=True, blank=True,)
    adress=models.ForeignKey(Adress,null=True, blank=True,on_delete=models.SET_NULL)
    transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL)
    certificate_type=models.CharField(max_length=15,null=True, blank=True,)
    session_key=models.CharField(max_length=100,null=True, blank=True,)
    user=models.ForeignKey(UserModel,blank=True,null=True,on_delete=models.SET_NULL)
    is_valid=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name +':'+ self.phone
    def amount_paid(self):
        tran=self.transaction
        return  tran.amount
    def transaction_id(self):
        tran=self.transaction
        str=""+format_html('<a href="%s" target="_blank">%s</a> || ' )  % (reverse("admin:payment_transaction_change", args=([tran.id])) , escape(tran.tran_id))
        return  format_html(str)
    
    def paid_at(self):
        tran=self.transaction
        return  tran.created_at
    
    def __unicode__(self):
        return self.name_bangla