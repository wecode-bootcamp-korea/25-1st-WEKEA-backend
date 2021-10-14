from django.urls import path

from product.views import SortItems

urlpatterns = [
    path('', SortItems.as_view()),
]
