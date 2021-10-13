import json

from django.http import JsonResponse
from django.views import View

from product.models import MainCategory, SubCategory, Product

class MainCategoryView(View):
    def get(self, request):
        main_categories = MainCategory.objects.all()

        return JsonResponse({ "main_categories" : list(main_categories.values('id', 'name')) }, status = 201)

class CategoryView(View):
    def get(self, request):
        main_categories = MainCategory.objects.all()

        result = [{
            "id"   : main_category.id,
            "name" : main_category.name,
            "sub"  : list(main_category.sub_categories.all().values('id', 'name'))
        } 
        for main_category in main_categories]

        return JsonResponse({"sub_categories" : result}, status = 200)

class ProductListView(View): # 특정 sub_category 요청시 해당하는 product 수정 요망 + 메인 페이지 product 랜덤 리스트 뽑기 + 제품 상세 페이지
    def get(self, request, id):
        sub_category = SubCategory.objects.get(id = id)
        products     = sub_category.products.all()
        results      = list(products.all().values('id',
                                                  'foreign_name', 
                                                  'korea_name', 
                                                  'information', 
                                                  'price')
                            )

        for result in results:
            result['images'] = list(products.get(id = result['id']).product_images.all().values('id', 'product_image'))
            result['size']   = list(products.get(id = result['id']).product_sizes.all().values('id', 'width','length','height'))

        return JsonResponse({"products": results}, status = 201)

class OneProductView(View):
    def get(self, request, id):
        product                 = Product.objects.filter(id = id)
        product_dict            = product.values('id', 
                                                    'foreign_name', 'korea_name', 'price', 'information', 'description'
        
        ).first()
        product_dict['main_category'] = { "id" : product.first().sub_category.id, "name" : product.first().sub_category.name}
        product_dict['sub_category']  = { "id" : product.first().sub_category.id, "name" : product.first().sub_category.name}
        product_dict['images']  = list(product.first().product_images.all().values('id', 'product_image'))
        product_dict['size']    = product.first().product_sizes.all().values('id', 'width', 'length' ,'height')[0]
        product_dict['reviews'] = list(product.first().reviews.all().values())

        return JsonResponse({'product' :  product_dict}, status = 200)
