from django.urls import path
from product.views import CategoryListView, ProductListView, ProductView, ProductFilter

urlpatterns = [
    path('/categories', CategoryListView.as_view()),
    path('/subcategories', ProductListView.as_view()),
    path('/<int:product_id>', ProductView.as_view()),
    path('', ProductFilter.as_view()),
]