from django.shortcuts import render

import json

from django.http  import JsonResponse
# from django.db    import transaction
from django.views import View

from product.models import MainCategory, SubCategory, Product, ProductImage, ProductSize




