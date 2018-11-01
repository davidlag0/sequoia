from django.db import models


class Store(models.Model):
    """This class represents the Store model."""
    name = models.CharField(max_length=255, blank=False, null=False,
        unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Account(models.Model):
    """This class represents the Account model."""
    name = models.CharField(max_length=255, blank=False, null=False,
        unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Category(models.Model):
    """This class represents the Category model."""
    name = models.CharField(max_length=255, blank=False, null=False,
        unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class SubCategory(models.Model):
    """This class represents the SubCategory model."""
    name = models.CharField(max_length=255, blank=False, null=False,
        unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class TransactionStatus(models.Model):
    """This class represents the TransactionStatus model."""
    name = models.CharField(max_length=255, blank=False, null=False,
        unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Transaction(models.Model):
    """This class represents the Transaction model."""
    transaction_date = models.DateTimeField('transaction date')
    original_description = models.CharField(blank=False, null=False,
        max_length=255)
    custom_description = models.CharField(blank=True, null=False,
        max_length=255)
    expense = models.DecimalField(blank=True, null=True,
        max_digits=8, decimal_places=2)
    revenue = models.DecimalField(blank=True, null=True,
        max_digits=8, decimal_places=2)
    store = models.ForeignKey(Store, blank=True, null=True,
        on_delete=models.PROTECT)
    account = models.ForeignKey(Account, blank=False, null=False,
        on_delete=models.PROTECT)
    category = models.ForeignKey(Category, blank=False, null=False,
        on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, blank=True, null=True,
        on_delete=models.PROTECT)
    transactionstatus = models.ForeignKey(TransactionStatus,
        blank=False, null=False, on_delete=models.PROTECT)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.custom_description


class Tag(models.Model):
    """This class represents the Tag model."""
    transaction_id = models.ForeignKey(Transaction, null=False,
        on_delete=models.PROTECT)
    tag_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.tag_name)
