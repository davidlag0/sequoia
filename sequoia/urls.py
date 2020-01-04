"""Application URL's"""
from django.contrib import admin
from django.urls import include, path
# from django.contrib.auth import views as auth_views
#from graphene_django.views import GraphQLView
#from sequoia.schema import schema
#from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # To test before removing the main app.
    # path('', include('main.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/password_reset/', auth_views.PasswordResetView.as_view(),
    # name='password_reset'),
    path('admin/', admin.site.urls),
    path('api/', include('transactions.urls')),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
