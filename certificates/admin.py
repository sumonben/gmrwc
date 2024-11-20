from django.contrib import admin
from .models import Certificate
from import_export.admin import ExportActionMixin,ImportExportMixin

# Register your models here.
@admin.register(Certificate)
class CertificateAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'name','email','phone','student_category','department','session','transaction','amount_paid','transaction_id','paid_at','is_valid']
    list_display_links = ['name','email','phone']
    list_filter=['session','group','class_year','is_valid']