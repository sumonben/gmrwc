from django.contrib import admin
from django.urls import path,include, re_path
from department import views
urlpatterns = [
    
    
    path('<str:navitem_name>/<str:navelement_head>/<str:heading>/<str:id>/',views.DepartmentPage, name='department'),


]