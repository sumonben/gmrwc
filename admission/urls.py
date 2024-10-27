from django.contrib import admin
from django.urls import path,include, re_path
from department import views 
import static
from . import views
from student import views as  view
from django.conf import settings
from django.conf.urls.static import static
from django import views as django_views

urlpatterns = [
    
    path('/login',views.admissionLogin, name='admission_login'),
    path('/admission-form', views.admissionForm, name="admission_form"),
    path('/admission-form-submit', views.admissionFormSubmit, name="admission_form_submit"),

    path('/jsi18n', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),






]