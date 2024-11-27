from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone', 'card_no', 'amount', 'tran_id','status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('currency', 'status')

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(PaymentGateway)

@admin.register(PaymentPurpose)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'id','serial','title','title_en']
    filter_fields=[  'id','title',]
