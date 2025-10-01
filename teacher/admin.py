from django.contrib import admin
from django.forms import Field
from .models import Teacher ,Designation,Position,BcsBatch, Committee
from import_export.admin import ExportActionMixin
from import_export.widgets import ManyToManyWidget
from import_export.resources import ModelResource
from import_export import fields, resources
from datetime import datetime
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)
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
    list_filter = (
        ('designation', RelatedDropdownFilter),
        ('t_department', RelatedDropdownFilter),

        ("first_joining_date", DateRangeFilterBuilder()),
        (
            "joining_date",
            DateTimeRangeFilterBuilder(
                title="Custom Title",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),
        #("batch",NumericRangeFilterBuilder),

        ("joining_date", DateRangeQuickSelectListFilterBuilder()),  # Range + QuickSelect Filter
        ('batch', RelatedDropdownFilter),

    )
    '''list_filter = (
        # for ordinary fields
        #('designation', DropdownFilter),
        # for choice fields
        #('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('designation', RelatedDropdownFilter),
    )'''
    save_as = True
    resource_class = StudentResource
    from_encoding = "utf-8"

@admin.register(Committee)
class CommitteeAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
    filter_horizontal = ['members_teacher','members_employee']


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

