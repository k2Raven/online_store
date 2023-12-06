from django.urls import path
from webapp.views import products_view, product_view, product_add_view, category_add_view

urlpatterns = [
    path('', products_view, name='index'),
    path('products/', products_view, name='products_view'),
    path('products/<int:pk>/', product_view, name='product_view'),
    path('products/add/', product_add_view, name='product_add_view'),
    path('categories/add/', category_add_view, name='category_add_view')
]
