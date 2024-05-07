from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 

class Product(models.Model):
    SALE = 'SALE'
    NEW = 'NEW'
    HOT = 'HOT'
    DISCOUNT = 'DISCOUNT'
    TAG_CHOICES = [
        (SALE, 'Sale'),
        (NEW, 'New'),
        (HOT, 'Hot'),
        (DISCOUNT, 'Discount'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255, choices=TAG_CHOICES, default=NEW)
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    seller = models.CharField(max_length=255)
    original_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    size_or_weight = models.CharField(max_length=255)
    quantity = models.IntegerField()
    product_type = models.CharField(max_length=255)
    manufacturing_date = models.DateField()
    lifespan = models.IntegerField()
    stocks_left = models.IntegerField()
    tags = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title