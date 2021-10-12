from django.db import models
from django.db.models.fields import related
from core.models import TimeStampModel

class User(TimeStampModel):
    last_name      = models.CharField(max_length = 20)
    first_name     = models.CharField(max_length = 20)
    gender         = models.IntegerField(null = False)
    email          = models.EmailField(unique = True)
    password       = models.CharField(max_length = 200)
    mobile_phone   = models.CharField(max_length = 11)
    favorite_store = models.IntegerField(null = False)
    birthday       = models.DateField()
    review         = models.ManyToManyField('product.Product', through = 'Review', related_name = 'review')
    cart           = models.ManyToManyField('product.Product', through = 'Cart', related_name = 'cart')

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.first_name

class Address(TimeStampModel):
    name_of_street  = models.CharField(max_length = 50)
    detail_address  = models.CharField(max_length = 20)
    zip_code        = models.IntegerField()
    default_address = models.BooleanField(default = False)
    user            = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'address')

    class Meta:
        db_table = 'addresses'
    
    def __str__(self):
        return self.name_of_street

class Review(TimeStampModel):
    text             = models.TextField()
    installation     = models.PositiveIntegerField()
    cost_performance = models.PositiveIntegerField()
    quality          = models.PositiveIntegerField()
    appearance       = models.PositiveIntegerField()
    functionality    = models.PositiveIntegerField()
    user             = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'reviews')
    product          = models.ForeignKey('product.Product', on_delete = models.CASCADE, related_name = 'reviews')

    class Meta:
        db_table = 'reviews'

class Cart(TimeStampModel):
    user     = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'carts')
    product  = models.ForeignKey('product.Product', on_delete = models.CASCADE, related_name = 'carts')
    quantity = models.IntegerField(default = 0)

    class Meta:
        db_table = 'carts'