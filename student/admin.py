from django.contrib import admin
from django.forms import Field
from .models import Student, StudentCategory,Class,Session,Group,Division,District,Upazilla,Union,GuardianInfo,Transaction,Adress,SubjectChoice,SscEquvalent
from import_export.admin import ExportActionMixin,ImportExportMixin
from import_export.widgets import ManyToManyWidget
from import_export.resources import ModelResource

# Register your models here.
class StudentResource(ModelResource):
    
    student_category = Field(
        widget=ManyToManyWidget(StudentCategory, field='title',
                                        separator='|')
    )
    class Meta:
        model = Student
        fields = ('email', 'student_category')


@admin.register(Student)
class StudentAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'name','email','phone','student_category','department','session','user_link']
    list_display_links = ['name','email']
    list_filter=['department','student_category','session','group','class_year','is_active']

@admin.register(GuardianInfo)
class GuardianInfoAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display= ['father_name', 'mother_name','guardian_phone']
    list_display_links = ['father_name', 'mother_name','guardian_phone']
    list_filter=['guardian_phone',]
@admin.register(SscEquvalent)
class SscEquvalentAdmin(ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(SubjectChoice)
class SubjectChoiceAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(Adress)
class AdressAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(Transaction)
class TransactionAdmin(ExportActionMixin,admin.ModelAdmin):
    pass


@admin.register(StudentCategory)
class StudentCategoryAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
    save_as = True
    resource_class = StudentResource
    

@admin.register(Division)
class DivisionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','link']
    list_display_links = ['name','name_en']
@admin.register(District)
class DistrictAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','division','link']
    list_display_links = ['name','name_en']
    list_filter=['division']

@admin.register(Upazilla)
class UpazillaAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','district','link']
    list_display_links = ['name','name_en']
    list_filter=['district']

@admin.register(Union)
class UnionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','upazilla','link']
    list_display_links = ['name','name_en']
    
