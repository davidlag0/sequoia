from django.contrib import admin

from .models import Store, Account, Category, SubCategory, TransactionStatus

admin.site.register(Store)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(TransactionStatus)
