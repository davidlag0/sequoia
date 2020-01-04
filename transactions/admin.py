"""Transactions admin.py"""
from django.contrib import admin

from .models import Store, Account, Category, SubCategory, TransactionStatus
from .models import Transaction, Tag

admin.site.register(Store)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(TransactionStatus)
admin.site.register(Transaction)
admin.site.register(Tag)
