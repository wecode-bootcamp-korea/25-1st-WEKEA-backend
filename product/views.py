import json

from django.http import JsonResponse
from django.views import View

from product.models import Product

class ReviewView(View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        reviews = list(product.reviews.all().values())

        return JsonResponse({"reviews": reviews}, status = 200)