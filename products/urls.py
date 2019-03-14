from django.urls import path
from .views import ListProductsView, DeleteAllProducts

urlpatterns = [
        path('products/', ListProductsView.as_view(), name='product-list'),
        path('products/delete', DeleteAllProducts.as_view(), name='product-delete'),
        ]
