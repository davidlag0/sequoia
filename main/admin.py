from django.contrib import admin

from .models import Transaction, Store, Account, Category, SubCategory, Status, Tag


class StoreInline(admin.TabularInline):
    model = Store
    #extra = 3


class AccountInline(admin.TabularInline):
    model = Account


class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transaction Date', {'fields': ['transaction_date'], 'classes': ['collapse']}),
        (None,               {'fields': ['report_description']}),
        (None,               {'fields': ['custom_description']}),
        (None,               {'fields': ['expense']}),
        (None,               {'fields': ['revenue']}),
    ]
    inlines = [StoreInline, AccountInline]
    list_display = ('transaction_date', 'custom_description', 'expense', 'revenue')
    #list_display = ('question_text', 'pub_date')
    #list_filter = ['pub_date']
    search_fields = ['transaction_date', 'report_description', 'custom_description', 'expense', 'revenue']

admin.site.register(Transaction, TransactionAdmin)
