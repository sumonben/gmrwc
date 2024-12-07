from django.contrib import admin
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Employee,Designation,Position,Type
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','employee_name','designation','position',]
    list_display_links = ['serial','employee_name']
@admin.register(Designation)
class TeacherDesignationAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
    
@admin.register(Position)
class TeacherPositionAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
    
@admin.register(Type)
class TeacherBcsBatchAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
