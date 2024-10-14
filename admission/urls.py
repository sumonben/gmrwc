from django.contrib import admin
from django.urls import path,include, re_path
from department import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('/',views.DepartmentPage, name='admission'),


]