from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    # extra fields for tracking
    category_is_active = models.BooleanField(default=True)
    category_created_by = models.CharField(max_length=255)
    category_updated_by = models.CharField(max_length=255)
    category_created_timestamp = models.DateField(default=timezone.now)
    #category_created_timestamp = models.DateTimeField(auto_now=True)
    category_updated_timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)

    sale = 'SALE'
    new = 'NEW'
    hot = 'HOT'
    discount = 'DISCOUNT'
    product_tag_choice = [
        (sale, 'Sale'),
        (new, 'New'),
        (hot, 'Hot'),
        (discount, 'Discount'),
    ]

    product_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='category_id')
    product_tag = models.CharField(
        max_length=255, choices=product_tag_choice, default=new)
    product_title = models.CharField(max_length=255)
    product_seller_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    product_discount = models.IntegerField()
    product_discounted_price = models.IntegerField(null=True)
    
    product_image = models.ImageField(upload_to='products/')
    product_description = models.TextField()
    product_manufacturing_date = models.DateField()
    product_lifespan = models.IntegerField()
    product_stocks_left = models.IntegerField()

    # extra fields for tracking
    category_is_active = models.BooleanField(default=True)
    category_created_by = models.CharField(max_length=255)
    category_updated_by = models.CharField(max_length=255)
    category_created_timestamp = models.DateField(default=timezone.now)
    category_updated_timestamp = models.DateField(default=timezone.now)

    @property
    def product_discounted_price(self):
        return ((self.product_price)*(self.product_discount))/10
    
    def __str__(self):
        return self.product_name
