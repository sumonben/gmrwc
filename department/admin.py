from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Department,Branch,Class,Session,Group,Subject
from import_export.admin import ExportActionMixin,ImportExportMixin

# Register your models here.
@admin.register(Department)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'serial','name','code','professor', 'associate_professor', 'assistant_professor','lecturer']
    list_filter=[  'name','code',]
    list_display_links = ['serial','name','code']

    fieldsets = ((None,{'fields': ('serial','name','name_en','code')}),
        ("পদসংখ্যাঃ", {
           'fields': ('professor', 'associate_professor', 'assistant_professor','lecturer')
        }),
        
    )
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=[  'serial','name','code',]
    list_filter=[  'name','code',]
    list_display_links = ['serial','name','code']

   

@admin.register(Branch)
class UserAdmin(admin.ModelAdmin):
    list_display=[   'serial','name','code']
    list_filter=[  'name','code',]
    list_display_links = ['serial','name','code']
    
@admin.register(Class)
class StudentClassAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']

@admin.register(Session)
class StudentSessionAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
@admin.register(Group)
class StudentGroupAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
