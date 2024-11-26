import string
import random
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
from .models import PaymentGateway



def generator_trangection_id( size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


    

def sslcommerz_payment_gateway(request, name, amount,student):
    
    print(student,amount)
    gateway = PaymentGateway.objects.all().first()
    cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
            
    sslcommez = SSLCOMMERZ(cradentials)
    body = {}
    body['student'] = student
    body['total_amount'] = amount
    body['currency'] = "BDT"
    body['tran_id'] = generator_trangection_id()
    body['success_url'] = 'https://test.gmrwc.edu.bd/payment/success/'
    body['fail_url'] = 'https://test.gmrwc.edu.bd/payment/payment/faild/'
    body['cancel_url'] = 'https://test.gmrwc.edu.bd/payment'
    body['emi_option'] = 0
    body['cus_name'] = name
    body['cus_email'] = 'request.data["email"]'
    body['cus_phone'] = student
    body['cus_add1'] = 'request.data["address"]'
    body['cus_city'] = 'request.data["address"]'
    body['cus_country'] = 'Bangladesh'
    body['shipping_method'] = "NO"
    body['multi_card_name'] = ""
    body['num_of_item'] = 1
    body['product_name'] = "Test"
    body['product_category'] = "Test Category"
    body['product_profile'] = "general"
    body['value_a'] = name
    body['value_b'] = student
    body['value_c'] = student
    


    response = sslcommez.createSession(body)
    #print(response)   
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]

def sslcommerz_payment_gateway_certificate(request, name, amount,phone,email,certificate_type):
    
    print(phone,amount)
    gateway = PaymentGateway.objects.all().first()
    cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
            
    sslcommez = SSLCOMMERZ(cradentials)
    body = {}
    body['student'] = name
    body['total_amount'] = amount
    body['currency'] = "BDT"
    body['tran_id'] = generator_trangection_id()
    body['success_url'] = 'http://localhost:8000/payment/success/'
    body['fail_url'] = 'http://localhost:8000/payment/payment/faild/'
    body['cancel_url'] = 'http://localhost:8000/payment'
    body['emi_option'] = 0
    body['cus_name'] = name
    body['cus_email'] = 'request.data["email"]'
    body['cus_phone'] = phone
    body['cus_add1'] = 'request.data["address"]'
    body['cus_city'] = 'request.data["address"]'
    body['cus_country'] = 'Bangladesh'
    body['shipping_method'] = "NO"
    body['multi_card_name'] = ""
    body['num_of_item'] = 1
    body['product_name'] = "Test"
    body['product_category'] = "Test Category"
    body['product_profile'] = "general"
    body['value_a'] = name
    body['value_b'] = phone
    body['value_c'] = email
    body['value_d'] = certificate_type

    


    response = sslcommez.createSession(body)
    #print(response)   
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]