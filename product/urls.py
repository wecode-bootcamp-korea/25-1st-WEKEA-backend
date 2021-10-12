from django.urls import path
from product.views import ReviewView

urlpatterns = [
    path('/<int:id>/reviews', ReviewView.as_view()),
]