"""
import datetime

from django.db import models
from django.utils import timezone


class Store(models.Model):
    store_name = models.CharField(max_length=200)

    class Meta:
        permissions = (("sequoia_admin", "Full access to Sequoia"),)

    def __str__(self):
        return self.store_name


class Account(models.Model):
    account_name = models.CharField(max_length=200)

    class Meta:
        permissions = (("sequoia_admin", "Full access to Sequoia"),)

    def __str__(self):
        return self.account_name


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        permissions = (("sequoia_admin", "Full access to Sequoia"),)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=200)

    class Meta:
        permissions = (("sequoia_admin", "Full access to Sequoia"),)

    def __str__(self):
        return self.subcategory_name


class Status(models.Model):
    status_name = models.CharField(max_length=200)

    class Meta:
        permissions = (("sequoia_admin", "Full access to Sequoia"),)

    def __str__(self):
        return self.status_name


class Transaction(models.Model):
    transaction_date = models.DateTimeField('transaction date')
    report_description = models.CharField(blank=False, null=False, max_length=200)
    custom_description = models.CharField(blank=True, null=False, max_length=200)
    expense = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    revenue = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    store = models.ForeignKey(Store, blank=True, null=True, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, blank=False, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        permissions = (("sequoia_admin", "Full access to Sequoia"),)

    def __str__(self):
        return self.custom_description

    #def was_published_recently(self):
    #    now = timezone.now()
    #    return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #was_published_recently.admin_order_field = 'pub_date'
    #was_published_recently.boolean = True
    #was_published_recently.short_description = 'Published recently?'


class Tag(models.Model):
    transaction = models.ForeignKey(Transaction, null=False, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=200)

    class Meta:
        permissions = (("sequoia_admin", "Full access to Sequoia"),)

    def __str__(self):
        return self.tag_name
"""