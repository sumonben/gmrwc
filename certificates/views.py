from django.http import HttpResponse
from django.shortcuts import render,redirect
from student.forms import SscEquvalentForm,SubjectChoiceForm,AdressForm
from .forms import ChoiceCertificateForm,CertificateForm
from department.models import Group
from .models import Certificate
from payment.sslcommerz import sslcommerz_payment_gateway,sslcommerz_payment_gateway_certificate
from django.views import View
from payment.models import Transaction
# Create your views here.

def ChoiceCertificate(request):
    form=ChoiceCertificateForm()
    return render(request,'certificate/choice_certificate.html',{'form':form})

def CertificateFormEntry(request):
    print(request.POST.get('student_category'))
    group=Group.objects.filter(id=request.POST.get('group')).first()
    print(group.title_en)
    form=CertificateForm(student_category=request.POST.get('student_category'))
    adress_form = AdressForm()
    student_category=request.POST.get('student_category')
    choice_certificate=request.POST.get('choice_certificate')
    context={'form':form,'adress_form':adress_form}
    context['student_category']=student_category
    context['choice_certificate']=choice_certificate
    print(student_category,choice_certificate)
    subject_form=SubjectChoiceForm(group=group)
    if request.POST.get('student_category') in '3':
        context['subject_form']=subject_form
       
        return render(request,'certificate/certificate_form_entry_hsc.html',context=context)
    return render(request,'certificate/certificate_form_entry_all.html',context=context)
  
def PayforCertificate(request):
    if request.method=="POST":
        form = CertificateForm(request.POST, request.FILES,student_category=1)
        form_adress = AdressForm(request.POST, request.FILES)

        if form.is_valid():
            certificate=form.save(commit=False)
            if form_adress.is_valid():
                adress=form_adress.save()
                certificate.adress=adress
            print(form_adress.errors)
            certificate.save()
        print(form.errors)


        return redirect(sslcommerz_payment_gateway_certificate(request,request.POST.get('name'), 100,request.POST.get('phone'),request.POST.get('email'),'certificate'))
       

class AuthenticateCertificate(View):
    model = Certificate
    template_name = 'certificate/authenticate_certificate.html'
    
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        context={}
        certificate=Certificate.objects.filter(email=request.POST.get('email'),phone=request.POST.get('phone'))
        context['certificate']=certificate
        return render(request,self.template_name,context)
    
def CreateCertificate(request):
    print(request.POST.get('tran_id'))

    if request.method=="POST":
        transaction=Transaction.objects.filter(tran_id=request.POST.get('tran_id').strip()).first()
        certificate=Certificate.objects.filter(transaction=transaction).first()
        print(certificate)
        if certificate.department:
            return render(request, 'certificate/others_testimonial.html',{'certificate':certificate})
        else:
            return render(request, 'certificate/hsc_testimonial.html',{'certificate':certificate})
    return render(request, 'certificate/hsc_testimonial.html',)


