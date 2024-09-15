from django.contrib import admin
from .models import Student, Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=[ 'name','email','phone','student_category','department','session','user_link']
    list_display_links = ['name','email']

@admin.register(Teacher)
class ProfileAdmin(admin.ModelAdmin):
    model = Teacher
    list_display=[ 't_name','t_email','t_phone','designation','t_department','batch']
