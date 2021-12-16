import json

from django.http  import JsonResponse

from django.views import View

from product.models import MainCategory, Product

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

class CategoryListView(View):
    def get(self, request):
        main_categories = MainCategory.objects.all().prefetch_related('sub_categories')

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
        try:
            sub_category_id = int(request.GET.get('sub_category_id', 1))
            sub_category = SubCategory.objects.get(id = sub_category_id)
            products = Product.objects.filter(sub_category_id = sub_category_id).\
                                    prefetch_related('product_sizes').\
                                    prefetch_related('product_images')

        except SubCategory.DoesNotExist:
            return JsonResponse({"message" : "SUB_CATEGORY_DOES_NOT_EXIST"}, status = 400)

        subcategory = {
            "id"          : sub_category.id,
            "name"        : sub_category.name,
            "description" : sub_category.description,
        }

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
            "subcategory" : subcategory,
            "products"    : products
        }
        
        return JsonResponse({"results" : results}, status = 200)

class ProductView(View):
    def get(self, request, product_id):
        products = Product.objects.filter(id = product_id).select_related('sub_category__main_category')

        if not products.exists():
            return JsonResponse({"message" : "PRODUCT_DOES_NOT_EXIST"}, status = 400)

        product  = products.first()

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