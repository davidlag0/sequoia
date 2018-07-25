from django.contrib import admin
from django import forms

from .models import Transaction, Store, Account, Category, SubCategory, Status, Tag


class TransactionAdminForm(forms.ModelForm):
    class Meta:
        model = Transaction

        fields = ("transaction_date",
                "report_description",
                "custom_description",
                "expense",
                "revenue",
                "store",
                "account",
                "category",
                "subcategory",
                "status")


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_date_formatted",
                    "custom_description",
                    "expense",
                    "revenue",
                    "store",
                    "account",
                    "category",
                    "subcategory",
                    "status")

    list_select_related = ("store",)

    """
    search_fields = ["transaction_date_formatted",
                    "report_description",
                    "custom_description",
                    "expense",
                    "revenue",
                    "store",
                    "account",
                    "category",
                    "subcategory",
                    "status"]
    """

    form = TransactionAdminForm

    def transaction_date_formatted(self, obj):
        return obj.transaction_date.strftime("%Y-%m-%d")

    transaction_date_formatted.admin_order_field = "transaction_date"
    transaction_date_formatted.short_description = "Date"

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Store)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Status)
admin.site.register(Tag)
