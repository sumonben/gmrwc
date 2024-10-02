from django.contrib import admin
from .models import Student, StudentCategory,Class,Session,Group
from import_export.admin import ExportActionMixin
# Register your models here.
@admin.register(Student)
class StudentAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'name','email','phone','student_category','department','session','user_link']
    list_display_links = ['name','email']
    list_filter=['department','student_category','session','group','class_year','is_active']


@admin.register(StudentCategory)
class StudentCategoryAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
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
