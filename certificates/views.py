from django.http import HttpResponse
from django.shortcuts import render,redirect
from student.forms import SscEquvalentForm,SubjectChoiceForm,AdressForm
from .forms import ChoiceCertificateForm,CertificateForm
from department.models import Group
from .models import Certificate
from teacher.models import Teacher
from payment.sslcommerz import sslcommerz_payment_gateway,sslcommerz_payment_gateway_certificate
from django.views import View
from payment.models import Transaction
import string
import random
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
from payment.models import PaymentGateway
from django.http import HttpResponseRedirect
from django.urls import reverse
from payment import sslcommerz 
from django.db import IntegrityError, transaction
from django.db.models import Q,Count
from account.models import UserModel
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def ChoiceCertificate(request):
    form=ChoiceCertificateForm()
    return render(request,'certificate/choice_certificate.html',{'form':form})

def CertificateFormEntry(request):
    print(request.POST.get('student_category'))
    form=CertificateForm(student_category=request.POST.get('student_category'),certificate_type=request.POST.get('certificate_type'))
    adress_form = AdressForm()
    student_category=request.POST.get('student_category')
    print(student_category)
    certificate_type=request.POST.get('certificate_type')
    context={'form':form,'adress_form':adress_form}
    context['student_category']=student_category
    context['choice_certificate']=certificate_type
    print(student_category,certificate_type)
    if request.POST.get('student_category') in '3':
        group=Group.objects.filter(id=request.POST.get('group')).first()
        subject_form=SubjectChoiceForm(group=group)
        context['subject_form']=subject_form
        return render(request,'certificate/certificate_form_entry_hsc.html',context=context)
    return render(request,'certificate/certificate_form_entry_all.html',context=context)


def PayforCertificate(request):
    context={}
    if request.method=="POST":
        form = CertificateForm(request.POST, request.FILES,student_category=request.POST.get('student_category'),certificate_type=request.POST.get('certificate_type'))
        form_adress = AdressForm(request.POST, request.FILES)
        subject=None
        if request.POST.get('student_category') is '3':
            group=Group.objects.filter(id=request.POST.get('group')).first()
            print(group)
            form_subjects = SubjectChoiceForm(request.POST,group=group)
            if form_subjects.is_valid():
                subject=form_subjects.save()


        if form.is_valid():
            certificate=form.save(commit=False)
            certificate.subjects=subject
            if form_adress.is_valid():
                if form_adress.is_valid():
                    adress=form_adress.save()
                    certificate.adress=adress

            '''cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
            
            sslcommez = SSLCOMMERZ(cradentials)
            body = {}
            body['student'] = request.POST.get('name')
            body['total_amount'] = 101.5
            body['currency'] = "BDT"
            body['tran_id'] = sslcommerz.generator_trangection_id()
            body['success_url'] = 'https://www.test.gmrwc.edu.bd/payment/success/'
            body['fail_url'] = 'https://www.test.gmrwc.edu.bd/payment/failed/'
            body['cancel_url'] = 'https://www.test.gmrwc.edu.bd/payment'
            body['emi_option'] = 0
            body['cus_name'] = request.POST.get('name')
            body['cus_email'] = request.POST.get('email')
            body['cus_phone'] = request.POST.get('phone')
            body['cus_add1'] = 'request.data["address"]'
            body['cus_city'] = 'request.data["address"]'
            body['cus_country'] = 'Bangladesh'
            body['shipping_method'] = "NO"
            body['multi_card_name'] = ""
            body['num_of_item'] = 1
            body['product_name'] = "Test"
            body['product_category'] = "Test Category"
            body['product_profile'] = "general"
            body['value_a'] = request.POST.get('name')
            body['value_b'] = request.POST.get('phone')
            body['value_c'] = request.POST.get('email')
            body['value_d'] = 1            

            response = sslcommez.createSession(body)
            certificate.session_key=response["sessionkey"]'''

            certificate.save()
            context['purpose']=1
            context['certificate_id']=certificate.id
            context['phone']=request.POST.get('phone')
            

            return render(request, 'certificate/success_certificate.html',context)
            #print(response["sessionkey"])   
            #return redirect('https://sandbox.sslcommerz.com/EasyCheckOut/testcde' + response["sessionkey"])


        print(form.errors)
        form=ChoiceCertificateForm()
        return render(request,'certificate/choice_certificate.html',{'form':form})
       

class AuthenticateCertificate(View):
    model = Certificate
    template_name = 'certificate/authenticate_certificate.html'
    
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        context={}
        certificate=Certificate.objects.filter(email=request.POST.get('email'),phone=request.POST.get('phone'), is_valid=True)
        context['certificate']=certificate
        return render(request,self.template_name,context)
    
def CreateCertificate(request):
    print(request.POST.get('tran_id'))

    if request.method=="POST":
        context={}
        transaction=Transaction.objects.filter(tran_id=request.POST.get('tran_id').strip()).first()
        print(transaction)
        principal=Teacher.objects.filter(position__serial=1, release_date=None,is_active=True).first()   
        context['principal']=principal
        certificate=Certificate.objects.filter(phone=request.POST.get('phone').strip(),id=request.POST.get('tran_id'),is_valid=True).first()
        context['certificate']=certificate

        if certificate:
            if certificate.certificate_type=='1':
                if certificate.student_category.id==3:
                    return render(request, 'certificate/hsc_testimonial.html',context)
                else:
                    return render(request, 'certificate/others_testimonial.html',context)
            elif certificate.certificate_type=='2':
                return render(request, 'certificate/character_certificate.html',context)
            elif certificate.certificate_type=='3':
                return render(request, 'certificate/leave_certificate.html',context)
            elif certificate.certificate_type=='4':
                return render(request, 'certificate/present_student_certificate.html',context)
            elif certificate.certificate_type=='5':
                return render(request, 'certificate/attestation_letter.html',context)

            else:
                return render(request, 'certificate/hsc_testimonial.html',context)
        '''if transaction:
            certificate=Certificate.objects.filter(phone=request.POST.get('phone').strip(),transaction=transaction).first()
            if certificate.certificate_type=='1':
                if certificate.student_category.id==3:
                    return render(request, 'certificate/hsc_testimonial.html',{'certificate':certificate})
                else:
                    return render(request, 'certificate/others_testimonial.html',{'certificate':certificate})
            elif certificate.certificate_type=='2':
                return render(request, 'certificate/character_certificate.html',{'certificate':certificate})
            elif certificate.certificate_type=='3':
                return render(request, 'certificate/leave_certificate.html',{'certificate':certificate})
            elif certificate.certificate_type=='4':
                return render(request, 'certificate/present_student_certificate.html',{'certificate':certificate})
            elif certificate.certificate_type=='5':
                return render(request, 'certificate/attestation_letter.html',{'certificate':certificate})

            else:
                return render(request, 'certificate/hsc_testimonial.html',{'certificate':certificate})'''
        not_found='Certificate not checked yet'
        context['not_found']=not_found

    return render(request, 'certificate/authenticate_certificate.html',context)


