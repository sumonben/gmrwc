from django.contrib import admin
from django.urls import path,include, re_path
from department import views as view
from teacher import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('teacher_details/<int:id>',views.teacherDetails, name='teacher_details'),
    path('teacherlist/<str:content_name>/<str:head>/<str:type>/<str:heading>/' ,views.teacherList, name='teacherlist'),
    path('teacher_vacant_post',views.TeacherVacantPost, name='teacher_vacant_post'),



]