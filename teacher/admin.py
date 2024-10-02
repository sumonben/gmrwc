from django.contrib import admin
from .models import Teacher ,Designation,Position,BcsBatch
from import_export.admin import ExportActionMixin
# Register your models here.
@admin.register(Teacher)
class ProfileAdmin(ExportActionMixin,admin.ModelAdmin):
    model = Teacher
    list_display=[ 't_name','t_email','t_phone','designation','t_department','batch']
    filter_horizontal=['branch',]
    list_filter=[  't_department','first_joining_date','designation','is_active']
@admin.register(Designation)
class TeacherDesignationAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
@admin.register(Position)
class TeacherPositionAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']

@admin.register(BcsBatch)
class TeacherBcsBatchAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']

