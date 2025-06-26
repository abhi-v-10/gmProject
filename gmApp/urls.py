from django.urls import path
from .views import *

urlpatterns = [
    path('api_listcreate/', ProductListCreateView.as_view(), name='ProductListCreateView'),
    path('api_retrieveupdatedestroy/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='ProductRetrieveUpdateDestroyView'),
    path('get_products/', get_products, name="get_products")
]
