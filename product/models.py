from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_image_url = models.URLField(default='abs')
    # extra fields for tracking
    category_is_active = models.BooleanField(default=True)
    category_created_by = models.CharField(max_length=255)
    category_updated_by = models.CharField(max_length=255)
    category_created_timestamp = models.DateTimeField(
        auto_now_add=True, editable=False)
    # category_created_timestamp = models.DateTimeField(auto_now=True)
    category_updated_timestamp = models.DateTimeField(
        auto_now_add=True, editable=False)

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
    # Linking to Category Schema
    product_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='category_id')

    product_tag = models.CharField(
        max_length=255, choices=product_tag_choice, default=new)
    product_seller_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    product_discount_percent = models.DecimalField(
        max_digits=3, decimal_places=2, default=0)
    product_discounted_price = models.IntegerField(null=True)

    product_image_url = models.URLField(default='abs')
    product_description = models.TextField()
    product_manufacturing_date = models.DateField()
    product_stocks_left = models.IntegerField()

    # extra fields for tracking
    category_is_active = models.BooleanField(default=True)
    category_created_by = models.CharField(max_length=255)
    category_updated_by = models.CharField(max_length=255)
    category_created_timestamp = models.DateTimeField(
        auto_now_add=True, editable=False)
    category_updated_timestamp = models.DateTimeField(
        auto_now_add=True, editable=False)

    @property
    def product_discounted_price(self):
        return (self.product_price - (self.product_price*(self.product_discount_percent/100)))

    def __str__(self):
        return f'{self.product_category} --> {self.product_name}'
