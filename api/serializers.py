from rest_framework import serializers
from .models import Store, Account, Category


class StoreSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Store
        fields = ('id', 'name')
        #read_only_fields = ('date_created', 'date_modified')


class AccountSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Account
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Category instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = ('id', 'name')

