from django.urls import path

from .views import ProductListCreateAPIView, \
    ProductRetrieveUpdateDestroyAPIView, \
    ProductCategoryListCreateAPIView, ProductCategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name="products"),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name="product"),
    path('product-categories/', ProductCategoryListCreateAPIView.as_view(), name="product_categories"),
    path('product-categories/<int:pk>/', ProductCategoryRetrieveUpdateDestroyAPIView.as_view(),
         name="product_category"),
]
