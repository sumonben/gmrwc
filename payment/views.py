from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic import View, TemplateView, DetailView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,HttpResponseNotFound
from .models import Transaction
from student.models import Student,GuardianInfo,SscEquvalent,SubjectChoice
from .sslcommerz import sslcommerz_payment_gateway
from sslcommerz_lib import SSLCOMMERZ 
from certificates.models import Certificate

class Index(TemplateView):
    template_name = "payment/index.html"

def DonateView(request):
    name = request.POST['name']
    amount = request.POST['amount']
    return redirect(sslcommerz_payment_gateway(request, name, amount))

def PaymentView(request,student,name,amount):
    name = request.POST['name']
    amount = request.POST['amount']
    return redirect(sslcommerz_payment_gateway(request, name, amount))


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutSuccessView(View):
    model = Transaction
    template_name = 'mainsite/carts/checkout-success.html'
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('nothing to see')

    def post(self, request, *args, **kwargs):
        

        data = self.request.POST
        certificate=Certificate.objects.filter(phone=data['value_b'],email=data['value_c']).last()
        transaction=None
        print(certificate)
        try:
            transaction=Transaction.objects.create(
                name = data['value_a'],
                phone=data['value_b'],
                email=data['value_c'],
                tran_id=data['tran_id'],
                val_id=data['val_id'],
                amount=data['amount'],
                card_type=data['card_type'],
                card_no=data['card_no'],
                store_amount=data['store_amount'],
                bank_tran_id=data['bank_tran_id'],
                status=data['status'],
                tran_date=data['tran_date'],
                currency=data['currency'],
                card_issuer=data['card_issuer'],
                card_brand=data['card_brand'],
                card_issuer_country=data['card_issuer_country'],
                card_issuer_country_code=data['card_issuer_country_code'],
                verify_sign=data['verify_sign'],
                verify_sign_sha2=data['verify_sign_sha2'],
                currency_rate=data['currency_rate'],
                risk_title=data['risk_title'],
                risk_level=data['risk_level'],

            )
            print(certificate,transaction)
            certificate.transaction=transaction
            certificate.save()

            messages.success(request,'Payment Successfull')
            student=Student.objects.filter(phone=data['value_b']).first()
            ssc_equivalent=SscEquvalent.objects.filter(student=student).first()
            subject_choice=SubjectChoice.objects.filter(student=student).first()
            print( student.department.name_en )
            if student.department.name_en is None:
                return render(request, 'student/testimony.html',{'student':student,'ssc_equivalent':ssc_equivalent,'subject_choice':subject_choice})
            else:
                return render(request, 'student/honstestimonial.html',{'student':student,'ssc_equivalent':ssc_equivalent,'subject_choice':subject_choice})
        except:
            messages.success(request,'Something Went Wrong')
        return render(request, 'certificate/success_certificate.html')


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'payment/failed.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)