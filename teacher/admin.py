from django.contrib import admin
from django.forms import Field
from .models import Teacher ,Designation,Position,BcsBatch
from import_export.admin import ExportActionMixin
from import_export.widgets import ManyToManyWidget
from import_export.resources import ModelResource
from import_export import fields, resources

# Register your models here.


class StudentResource(ModelResource):
    
    position = fields.Field( column_name='Position',attribute='position',
        widget=ManyToManyWidget(Position, field='title',
                                        separator='|')
    )
    class Meta:
        model = Teacher

@admin.register(Teacher)
class ProfileAdmin(ExportActionMixin,admin.ModelAdmin):
    model = Teacher
    list_display=[ 't_name','t_email','t_phone','designation','t_department','batch']
    filter_horizontal=['position','branch',]
    list_filter=[  't_department','first_joining_date','designation','is_active']
    save_as = True
    resource_class = StudentResource
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

