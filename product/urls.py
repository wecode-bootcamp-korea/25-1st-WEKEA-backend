from django.urls import path
from product.views import CategoryListView, ProductListView, ProductView, SortItems

urlpatterns = [
    path('/categories', CategoryListView.as_view()),
    path('/subcategories', ProductListView.as_view()),
    path('/<int:product_id>', ProductView.as_view()),
    path('', SortItems.as_view()),
]
