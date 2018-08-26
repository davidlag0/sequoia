from rest_framework import generics
from .serializers import StoreSerializer, AccountSerializer
from .serializers import CategorySerializer, SubCategorySerializer
from .serializers import TransactionStatusSerializer
from .models import Store, Account, Category, SubCategory, TransactionStatus


class StoreCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of a store in our rest api."""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new store."""
        serializer.save()


class StoreDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests of a store."""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class AccountCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of an account in our rest api."""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new account."""
        serializer.save()


class AccountDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests of an account."""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CategoryCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of a category in our rest api."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new category."""
        serializer.save()


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests of a category."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of a subcategory in our rest api."""
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new subcategory."""
        serializer.save()


class SubCategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests of a subcategory."""
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class TransactionStatusCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of a transactionstatus in our rest api."""
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new transactionstatus."""
        serializer.save()


class TransactionStatusDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests of a transactionstatus."""
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer

