from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Department,Branch
# Register your models here.
@admin.register(Department)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'serial','name','code',]
    list_filter=[  'name','code',]

@admin.register(Branch)
class UserAdmin(admin.ModelAdmin):
    list_display=[   'serial','name','code',]
    list_filter=[  'name','code',]
'''@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=[ 'name','email','phone','student_category','department','session']

'''