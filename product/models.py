from django.db import models

class Group(models.Model):
    name = models.CharField(max_length = 20)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'groups'
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 150)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'categories'
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    foreign_name = models.CharField(max_length = 20)
    korea_name   = models.CharField(max_length = 20)
    price        = models.DecimalField(max_digits = 10, decimal_places = 2)
    information  = models.CharField(max_length = 30)
    is_deleted = models.BooleanField(default= False)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.korea_name
        
class ProductImage(models.Model):
    product_image = models.CharField(max_length = 200)
    is_deleted = models.BooleanField(default= False)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_images'

class ProductSize(models.Model):
    width      = models.DecimalField(max_digits = 10, decimal_places = 2)
    length     = models.DecimalField(max_digits = 10, decimal_places = 2)
    height     = models.DecimalField(max_digits = 10, decimal_places = 2)
    size_image = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_sizes'