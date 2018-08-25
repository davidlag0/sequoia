from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StoreCreateView, StoreDetailsView
from .views import AccountCreateView, AccountDetailsView
from .views import CategoryCreateView, CategoryDetailsView


urlpatterns = {
    url(r'^stores/$', StoreCreateView.as_view(), name="create_store"),
    url(r'^stores/(?P<pk>[0-9]+)/$',
        StoreDetailsView.as_view(), name="details_store"),
    url(r'^accounts/$', AccountCreateView.as_view(), name="create_account"),
    url(r'^accounts/(?P<pk>[0-9]+)/$',
        AccountDetailsView.as_view(), name="details_account"),
    url(r'^categories/$', CategoryCreateView.as_view(), name="create_category"),
    url(r'^categories/(?P<pk>[0-9]+)/$',
        CategoryDetailsView.as_view(), name="details_category"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
