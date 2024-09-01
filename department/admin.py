from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=[ 'name','email','phone','student_category','department','session']

