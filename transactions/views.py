"""""Transactions API Views"""
from rest_framework import filters
from rest_framework import viewsets
from .serializers import StoreSerializer, AccountSerializer
from .serializers import CategorySerializer, SubCategorySerializer
from .serializers import TransactionStatusSerializer
from .serializers import TransactionSerializer, TagSerializer
from .models import Store, Account, Category, SubCategory
from .models import TransactionStatus, Transaction, Tag


class StoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class AccountViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class TransactionStatusViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
