"""Transactions API URL's"""
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import StoreCreateView, StoreDetailsView
from .views import AccountCreateView, AccountDetailsView
from .views import CategoryCreateView, CategoryDetailsView
from .views import SubCategoryCreateView, SubCategoryDetailsView
from .views import TransactionStatusCreateView, TransactionStatusDetailsView
from .views import TransactionCreateView, TransactionDetailsView
from .views import TagCreateView, TagDetailsView
from .views import TransactionsView


urlpatterns = {
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),

    url(r'^stores/$', StoreCreateView.as_view(),
        name="create_store"),
    url(r'^stores/(?P<pk>[0-9]+)/$', StoreDetailsView.as_view(),
        name="details_store"),

    url(r'^accounts/$', AccountCreateView.as_view(),
        name="create_account"),
    url(r'^accounts/(?P<pk>[0-9]+)/$', AccountDetailsView.as_view(),
        name="details_account"),

    url(r'^categories/$', CategoryCreateView.as_view(),
        name="create_category"),
    url(r'^categories/(?P<pk>[0-9]+)/$',
        CategoryDetailsView.as_view(), name="details_category"),

    url(r'^subcategories/$', SubCategoryCreateView.as_view(),
        name="create_subcategory"),
    url(r'^subcategories/(?P<pk>[0-9]+)/$',
        SubCategoryDetailsView.as_view(),
        name="details_subcategory"),

    url(r'^transaction_statuses/$',
        TransactionStatusCreateView.as_view(),
        name="create_transactionstatus"),
    url(r'^transaction_statuses/(?P<pk>[0-9]+)/$',
        TransactionStatusDetailsView.as_view(),
        name="details_transactionstatus"),

    url(r'^transactions/$', TransactionCreateView.as_view(),
        name="create_transaction"),

    url(r'^transactions/(?P<pk>[0-9]+)/$',
        TransactionDetailsView.as_view(),
        name="details_transaction"),

    url(r'^tags/$', TagCreateView.as_view(),
        name="create_tag"),
    url(r'^tags/(?P<pk>[0-9]+)/$', TagDetailsView.as_view(),
        name="details_tag"),

    path('', TransactionsView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
