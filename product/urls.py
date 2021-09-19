from django.urls import path

from product.views import ProductsListView, ProductDetailView, CreateProductView, UpdateProductView, \
    DeleteProductView

urlpatterns = [
    path('products/', ProductsListView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('products/create/', CreateProductView.as_view()),
    path('products/update/<int:id>/', UpdateProductView.as_view()),
    path('products/delete/<int:id>/', DeleteProductView.as_view()),
]