from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic import View, TemplateView, DetailView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,HttpResponseNotFound
from .models import Transaction,PaymentPurpose
from student.models import Student,GuardianInfo,SscEquvalent,SubjectChoice
from .sslcommerz import sslcommerz_payment_gateway
from sslcommerz_lib import SSLCOMMERZ 
from certificates.models import Certificate
from student.models import Student
from account.models import UserModel

cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
            
sslcommez = SSLCOMMERZ(cradentials)

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
        
        context={}
        data = self.request.POST
        tran_purpose=PaymentPurpose.objects.filter(id=data['value_d']).first()
        context['tran_purpose']=tran_purpose
        print(data)
        transaction=None
        try:
            transaction=Transaction.objects.create(
                name = data['value_a'],
                phone=data['value_b'],
                email=data['value_c'],
                tran_id=data['tran_id'],
                tran_purpose=tran_purpose,
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
            print("data['value_d']:",data['value_d'])
            if data['value_d'] == '1':
                certificate=Certificate.objects.filter(phone=data['value_b'],email=data['value_c']).last()
                print(certificate,transaction)
                certificate.transaction=transaction
                certificate.save()
                certificates=Certificate.objects.filter(phone=data['value_b'],email=data['value_c'],tran_id=None)
                for cert in certificates:
                    cert.delete()

                print("Certificate:",1)
                context['purpose']=1

            if data['value_d'] == '2':
                student=Student.objects.filter(phone=data['value_b']).last()
                password="Student@"+data['value_b']
                user = UserModel.objects.create_user(username=data['value_b'],
                                 email=data['value_c'],last_name="Student",
                                 password=password,is_active=False)
                student.user=user
                student.save()
                students=Student.objects.filter(phone=data['value_b'],user=None)
                for std in students:
                    std.delete()

                print(student)
                context['purpose']=2
                context['student']=student.phone
            messages.success(request,'Payment Successful!!')
            
        except:
            messages.success(request,'Something Went Wrong')
            context['messages']=messages
        return render(request, 'certificate/success_certificate.html',context)




@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'payment/failed.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data=request.POST
        context={}
        tran_purpose=PaymentPurpose.objects.filter(id=data['value_d']).first()
        context['tran_purpose']=tran_purpose
        
        if data['value_d'] == '1':
            certificate=Certificate.objects.filter(phone=data['value_b'],transaction=None)
            if certificate:
                certificate.delete()
        if data['value_d'] == '2':
            student=Student.objects.filter(phone=data['value_b']).first()
            #user=UserModel.objects.filter(username=data['value_b']).first()
            #user.delete()

        '''certificate=Certificate.objects.filter(transaction=None)
        print(request.POST)
        
        for cert in certificate:
            response = sslcommez.transaction_query_session(cert.session_key)
            print(response['status'])
            print(response)

            if response['status'] in 'FAILED' or response['status'] in 'PENDING':
                cert.delete()'''
        return render(request, self.template_name,context)
