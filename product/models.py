from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_is_active = models.BooleanField(default=True)
    category_updated_date = models.DateTimeField(default=timezone.now)
    category_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_is_active = models.BooleanField(default=True)
    product_created_date = models.DateTimeField(detault=timezone.now)
    product_updated_date = models.DateTimeField(default=timezone.now)

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
    product_rating = models.DecimalField(
        max_digits=3, decimal_places=2, default=0)
    product_seller_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/')
    product_description = models.TextField()
    product_manufacturing_date = models.DateField()
    product_lifespan = models.IntegerField()
    product_stocks_left = models.IntegerField()

    def __str__(self):
        return self.product_name
