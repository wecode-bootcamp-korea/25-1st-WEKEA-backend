import json

from django.http  import JsonResponse
from django.db.models import Q

from django.views import View

from product.models import MainCategory, SubCategory, Product, ProductImage, ProductSize

class SortItems(View):
    def get(self, request):
        sub_category_products = request.GET.get('products_list')
        sort                  = request.GET.get('sort')

        sort_set = {
            'price_low_to_high': 'price',
            'price_high_to_low': '-price',
            'name_ascending': '-korea_name',
        }

        products = Product.objects.filter(sub_category=sub_category_products).order_by(sort_set.get(sort), 'id')

        results = [{
            'product_id': product.id,
            'korea_name': product.korea_name,
            'foreign_name': product.foreign_name,
            'price' : product.price,
            'information': product.information,
            'is_deleted': product.is_deleted,
            'sizes' : [
                {
                    "id" : size.id,
                    "width" : size.width,
                    "length": size.length
                } for size in product.product_sizes.all()
            ],
            'images': [
                {
                    "product_image": product_images.product_image,
                } for product_images in product.product_images.all()
            ] 
        } for product in products]
            
        return JsonResponse({'results': results }, status=200)