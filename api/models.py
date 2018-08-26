from django.db import models


class Store(models.Model):
    """This class represents the Store model."""
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Account(models.Model):
    """This class represents the Account model."""
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Category(models.Model):
    """This class represents the Category model."""
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class SubCategory(models.Model):
    """This class represents the SubCategory model."""
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class TransactionStatus(models.Model):
    """This class represents the TransactionStatus model."""
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
