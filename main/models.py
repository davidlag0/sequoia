import datetime

from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    transaction_date = models.DateTimeField('transaction date')
    report_description = models.CharField(max_length=200)
    custom_description = models.CharField(max_length=200)
    expense = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    revenue = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    def __str__(self):
        return self.custom_description
    #def was_published_recently(self):
    #    now = timezone.now()
    #    return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #was_published_recently.admin_order_field = 'pub_date'
    #was_published_recently.boolean = True
    #was_published_recently.short_description = 'Published recently?'


class Store(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=200)
    def __str__(self):
        return self.store_name


class Account(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200)
    def __str__(self):
        return self.account_name


class Category(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=200)
    def __str__(self):
        return self.subcategory_name


class Status(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    status_name = models.CharField(max_length=200)
    def __str__(self):
        return self.status_name


class Tag(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=200)
    def __str__(self):
        return self.tag_name
