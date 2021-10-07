from django.db import models

class User(models.Model):
    last_name      = models.CharField(max_length = 20)
    first_name     = models.CharField(max_length = 20)
    age            = models.IntegerField()
    email          = models.EmailField()
    password       = models.CharField(max_length = 200)
    mobile_phone   = models.CharField(max_length = 11)
    favorite_store = models.CharField(max_length = 20)
    birthday       = models.DateField()
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)

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
    creatd_at       = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'addresses'
    
    def __str__(self):
        return self.name_of_street

class Review(models.Model):
    text = models.TextField(max_length = 50)
    assemblyInstruction = models.IntegerField()
    costPerformance = models.IntegerField()
    quality         = models.IntegerField()
    exterior        = models.IntegerField()
    functionality   = models.IntegerField()
    user            = models.ForeignKey('user', on_delete = models.CASCADE)
    product         = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    creatd_at       = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'reviews'

class Cart(models.Model):
    user       = models.OneToOneField('User', on_delete = models.CASCADE, related_name = 'cart')
    product    = models.ManyToManyField('product.Product',related_name = 'product', through = 'Cart_Product')
    quantity   = models.IntegerField()
    creatd_at  = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'carts'

class Cart_Product(models.Model):
    product    = models.ForeignKey('product.Product', related_name = 'product')
    user       = models.ForeignKey('User', related_name = 'user')
    creatd_at  = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'cart_product'