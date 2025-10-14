from django.contrib import admin
from .models import Transaction
# Register your models here.
from django.contrib import admin

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('money_in', 'money_out', 'current_balance', 'category', 'tag', 'payee', 'transaction_date', 'account', 'description', 'cleared')



admin.site.register(Transaction, TransactionAdmin)