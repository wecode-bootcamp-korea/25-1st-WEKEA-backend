from django.db import models

from core.models import TimeStampModel

class Group(TimeStampModel):
    name = models.CharField(max_length = 20)
    
    class Meta:
        db_table = 'groups'
    
    def __str__(self):
        return self.name

class Category(TimeStampModel):
    name        = models.CharField(max_length = 20)
    description = models.CharField(max_length = 150)
    group       = models.ForeignKey('Group', on_delete = models.CASCADE, related_name = 'categories')
    is_deleted   = models.BooleanField(default= False)

    class Meta:
        db_table = 'categories'
    
    def __str__(self):
        return self.name
        
class Product(TimeStampModel):
    foreign_name = models.CharField(max_length = 20)
    korea_name   = models.CharField(max_length = 20)
    price        = models.DecimalField(max_digits = 10, decimal_places = 2)
    information  = models.CharField(max_length = 30)
    is_deleted   = models.BooleanField(default = False)
    category     = models.ForeignKey('Category', on_delete = models.CASCADE, related_name = 'products')
    
    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.korea_name

class ProductImage(TimeStampModel):
    product_image = models.CharField(max_length = 200)
    is_deleted  = models.BooleanField(default= False)
    product     = models.ForeignKey('product', on_delete = models.CASCADE, related_name = 'productImages')
    
    class Meta:
        db_table = 'product_images'

class ProductSize(TimeStampModel):
    width      = models.DecimalField(max_digits = 10, decimal_places = 2)
    length     = models.DecimalField(max_digits = 10, decimal_places = 2)
    height     = models.DecimalField(max_digits = 10, decimal_places = 2)
    size_image = models.CharField(max_length = 200)
    product     = models.ForeignKey('product', on_delete = models.CASCADE, related_name = 'productSizes')
    
    class Meta:
        db_table = 'product_sizes'