from django.contrib import admin
from django.urls import path,include, re_path
from department import views
urlpatterns = [
    
    
    path('<str:navitem_name>/<str:navelement_head>/<str:heading>/<str:id>/',views.DepartmentPage, name='department'),
    path('<int:departmentId>/<str:navitem_name>/',views.departmentItems, name='department-nav'),
    path('single-notice-department/<int:departmentId>/<int:id>/', views.singleNoticeDepartment, name="single_notice_department"),


]