from django.urls import path
from product.views import MainCategoryView, CategoryView, ProductListView, OneProductView

urlpatterns = [
    path('/categories', CategoryView.as_view()),
    path('/subcategories/<int:subcategory_id>', ProductListView.as_view()),
    path('/<int:product_id>', OneProductView.as_view()),
]