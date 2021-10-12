from django.urls import path
from product.views import MainCategoryView, SubCategoryView, ProductView, OneProductView

urlpatterns = [
    path('/maincategories', MainCategoryView.as_view()),
    path('/subcategories', SubCategoryView.as_view()),
    path('/products/<int:id>', ProductView.as_view()),
    path('/<int:id>', OneProductView.as_view()),
]