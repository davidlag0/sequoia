from rest_framework import serializers
from .models import Store, Account, Category, SubCategory, TransactionStatus
from .models import Transaction, Tag


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


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer to map the SubCategory instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = SubCategory
        fields = ('id', 'name')


class TransactionStatusSerializer(serializers.ModelSerializer):
    """Serializer to map the TransactionStatus instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = TransactionStatus
        fields = ('id', 'name')


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer to map the Transaction instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transaction
        fields = ('id', 'transaction_date', 'original_description', \
            'custom_description', 'expense', 'revenue', 'store', \
            'account', 'category', 'subcategory', 'transactionstatus')


class TagSerializer(serializers.ModelSerializer):
    """Serializer to map the Tag instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Tag
        fields = ('id', 'tag_name', 'transaction_id')
