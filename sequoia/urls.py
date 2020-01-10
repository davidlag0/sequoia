"""Application URL's"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
#from graphene_django.views import GraphQLView
#from sequoia.schema import schema
#from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openapi/',
         get_schema_view(title="Sequoia API",
                         description="API for Sequoia Back-End"
                        ),
         name='openapi-schema'),
    path('doc/',
         TemplateView.as_view(template_name='redoc/redoc.html',
                              extra_context={'schema_url':'openapi-schema'}
                             ),
         name='redoc'),
    path('api/transactions/', include('transactions.urls')),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
