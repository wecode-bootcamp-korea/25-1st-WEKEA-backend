import json

from django.db.models.query_utils import Q
from django.http                  import JsonResponse
from django.views                 import View

from product.models import MainCategory, Product

class ProductFilter(View):
    def get(self, request):
        sub_category_products = request.GET.get('products_list')
        sort                  = request.GET.get('sort')
        search                = request.GET.get('search')

        sort_set = {
            'best'            : 'id',
            'price_ascending': 'price',
            'price_descending': '-price',
            'name_ascending'   : 'korea_name',
            'name_descending'  : '-korea_name',
            'created_ascending': 'created_at',
            'created_decending': '-created_at',
        }

        product_list = Q()

        if sub_category_products:
            product_list.add(Q(sub_category=sub_category_products), Q.AND)

        if search:
            product_list.add(Q(korea_name__icontains=search)\
                |Q(sub_category__name__icontains=search), Q.AND)

        products = Product.objects.filter(product_list)\
            .order_by(sort_set.get(sort, 'id'))

        results = [{
            'product_id'  : product.id,
            'korea_name'  : product.korea_name,
            'foreign_name': product.foreign_name,
            'price'       : product.price,
            'information' : product.information,
            'is_deleted'  : product.is_deleted,
            'sizes' : [
                {
                    "id"    : size.id,
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
            
        return JsonResponse({'results': results }, status = 200)
class CategoryListView(View):
    def get(self, request):
        main_categories = MainCategory.objects.all()

        result = [{
            "id"   : main_category.id,
            "name" : main_category.name,
            "sub_categories"  : [{
                "id"   : sub_category.id,
                "name" : sub_category.name
            } for sub_category in main_category.sub_categories.all()]
        } for main_category in main_categories]

        return JsonResponse({"main_categories" : result}, status = 200)

class ProductListView(View): 
    def get(self, request):
        sub_category_id = int(request.GET.get('sub_category_id', None))
        products = Product.objects.filter(sub_category_id = sub_category_id)
        sub_category = products.first().sub_category

        products = [{
            "product_id"   : product.id,
            "foreign_name" : product.foreign_name,
            "korea_name"   : product.korea_name,
            "information"  : product.information,
            "price"        : product.price,
            "images"       : [{
                "id"            : image.id,
                "product_image" : image.product_image,
                } for image in product.product_images.all()],
            "sizes"        : [{
                "id"     : size.id,
                "width"  : size.width,
                "length" : size.length,
                "height" : size.height,
                } for size in product.product_sizes.all()] 
        } for product in products]

        results = {
            "subcategory" : {
                "id"          : sub_category.id,
                "name"        : sub_category.name,
                "description" : sub_category.description,
            },
            "products"    : products
        }
        
        return JsonResponse({"results" : results}, status = 200)

class ProductView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id = product_id)

        result = {
            "id"            : product.id,
            "foreign_name"  : product.foreign_name,
            "korea_name"    : product.korea_name,
            "price"         : product.price,
            "information"   : product.information,
            "description"   : product.description,
            "main_category" : {
                "id"   : product.sub_category.main_category.id,
                "name" : product.sub_category.main_category.name,
            },
            "sub_category"  : {
                "id"   : product.sub_category.id,
                "name" : product.sub_category.name,
                "description" : product.sub_category.description,
            },
            "reviews" : [{
                "id"               : review.id,
                "review"           : review.text,
                "installation"     : review.installation,
                "cost_performance" : review.cost_performance,
                "quality"          : review.quality,
                "appearance"       : review.appearance,
                "functionality"    : review.functionality,
                "created_at"       : review.created_at,
                } for review in product.reviews.all()],
            "images" : [{
                "id"            : image.id,
                "product_image" : image.product_image,
                } for image in product.product_images.all()],
            "sizes" : [{
                "id"     : size.id,
                "width"  : size.width,
                "length" : size.length,
                "height" : size.height,
                } for size in product.product_sizes.all()]
        }

        return JsonResponse({'product' : result}, status = 200)
