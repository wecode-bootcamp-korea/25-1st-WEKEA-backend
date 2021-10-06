from django.db import models

class User(models.Model):
    last_name      = models.CharField(max_length = 20)
    first_name     = models.CharField(max_length = 30)
    age            = models.IntegerField()
    email          = models.EmailField()
    password       = models.CharField(max_length = 200)
    mobile_phone   = models.CharField(max_length = 11)
    favorite_store = models.CharField(max_length = 30)
    birthday       = models.DateField()
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)

    class Meta:
        db_tables = 'users'
    
    def __str__(self):
        return self.first_name

class Address(models.Model):
    name_of_street = models.CharField(max_length = 50)
    detail_address = models.CharField(max_length = 30)
    zip_code       = models.IntegerField()
    default        = models.BooleanField()
    creatd_at      = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)

    class Meta:
        db_tables = 'addresses'
    
    def __str__(self):
        return self.name_of_street