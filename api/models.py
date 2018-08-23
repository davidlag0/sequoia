from django.db import models


class Store(models.Model):
    """This class represents the Store model."""
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Account(models.Model):
    """This class represents the Account model."""
    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

