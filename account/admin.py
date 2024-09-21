from django.contrib import admin
from .models import Student, Teacher
from import_export.admin import ExportActionMixin
# Register your models here.
@admin.register(Student)
class StudentAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'name','email','phone','student_category','department','session','user_link']
    list_display_links = ['name','email']
    list_filter=['department','student_category','session','group','class_year','is_active']

@admin.register(Teacher)
class ProfileAdmin(ExportActionMixin,admin.ModelAdmin):
    model = Teacher
    list_display=[ 't_name','t_email','t_phone','designation','t_department','batch']
    filter_horizontal=['branch',]
    list_filter=[  't_department','first_joining_date','designation','is_active']

    
