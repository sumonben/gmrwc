from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Department,Branch
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

@admin.register(Branch)
class UserAdmin(admin.ModelAdmin):
    list_display=[   'serial','name','code']
    list_filter=[  'name','code',]
    list_display_links = ['serial','name','code']
