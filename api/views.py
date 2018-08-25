from rest_framework import generics
from .serializers import StoreSerializer, AccountSerializer
from .serializers import CategorySerializer
from .models import Store, Account, Category


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

