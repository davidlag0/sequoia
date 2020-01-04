"""Transactions API URL's"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transactions import views


ROUTER = DefaultRouter()
ROUTER.register(r'stores', views.StoreViewSet)
ROUTER.register(r'accounts', views.AccountViewSet)
ROUTER.register(r'categories', views.CategoryViewSet)
ROUTER.register(r'subcategories', views.SubCategoryViewSet)
ROUTER.register(r'transaction_statuses', views.TransactionStatusViewSet)
ROUTER.register(r'transactions', views.TransactionViewSet)
ROUTER.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
]
