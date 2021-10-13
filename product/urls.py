from django.urls import path
from product.views import MainCategoryView, CategoryView, ProductListView, OneProductView

urlpatterns = [
    path('/categories', CategoryView.as_view()),
    path('/subcategories/<int:id>', ProductListView.as_view()),
    path('/<int:id>', OneProductView.as_view()),
]