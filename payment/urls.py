from django.contrib import admin
from django.urls import path,include, re_path
from department import views 
import static
from . import views
from student import views as  view
from django.conf import settings
from django.conf.urls.static import static
from django import views as django_views
from . import views
urlpatterns = [
    
    path('', views.Index.as_view(), name='payment'),
    path('transaction/', views.DonateView, name='transaction'),
    path('success/', views.CheckoutSuccessView.as_view(), name='success'),
    path('failed/', views.CheckoutFaildView.as_view(), name='faild'),
    





]