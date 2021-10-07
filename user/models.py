from django.db import models

class User(models.Model):
    last_name      = models.CharField(max_length = 20)
    first_name     = models.CharField(max_length = 20)
    age            = models.PositiveIntegerField()
    email          = models.EmailField(unique = True)
    password       = models.CharField(max_length = 200)
    mobile_phone   = models.CharField(max_length = 11)
    favorite_store = models.CharField(max_length = 20)
    birthday       = models.DateField()
    review         = models.ManyToManyField('Product', through = 'Reivew')

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.first_name

class Address(models.Model):
    name_of_street  = models.CharField(max_length = 50)
    detail_address  = models.CharField(max_length = 20)
    zip_code        = models.IntegerField()
    default_address = models.BooleanField(default = False)
    user            = models.ForeignKey('User', on_delete = models.CASCADE)

    class Meta:
        db_table = 'addresses'
    
    def __str__(self):
        return self.name_of_street

class Review(models.Model):
    text             = models.TextField(max_length = 50)
    installation     = models.PositiveIntegerField()
    cost_performance = models.PositiveIntegerField()
    quality          = models.PositiveIntegerField()
    appearance       = models.PositiveIntegerField()
    functionality    = models.PositiveIntegerField()
    user             = models.ForeignKey('User', on_delete = models.CASCADE)
    product          = models.ForeignKey('product.Product', on_delete = models.CASCADE)

    class Meta:
        db_table = 'reviews'

class Cart(models.Model):
    user     = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'carts')
    product  = models.ForeignKey('product.Product', on_delete = models.CASCADE, related_name = 'products')
    quantity = models.IntegerField(default = 0)

    class Meta:
        db_table = 'carts'