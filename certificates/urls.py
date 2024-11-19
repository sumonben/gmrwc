from django.contrib import admin
from django.urls import path,include, re_path
import static
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django import views as django_views

urlpatterns = [
    
    path('choice-certificate/',views.ChoiceCertificate, name='choice-certificate'),
    path('choice-form-entry/',views.CertificateFormEntry, name='choice-form-entry'),

    path('payfor-certificate/', views.PayforCertificate, name="payfor-certificate"),
    #path('admission_form_submit/', views.admissionFormSubmit, name="admission_form_submit"),
    #path('form-download/', views.formDownload, name='form-download'),

    path('jsi18n/', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),






]