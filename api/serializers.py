from rest_framework import serializers
from product.models import Product, Category, Cart, CartItem
from django.contrib.auth import get_user_model
from collections import defaultdict


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  # else sepcified field add in ['field name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"  # else sepcified field add in ['field name']


User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name',
                  'product_category', 'product_tag_choice']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_items = serializers.SerializerMethodField()
    total_cart_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['cart_id', 'items', 'total_items', 'total_cart_price']

    def get_items(self, obj):
        items = obj.items.all()
        if not items:
            return []

        serialized_items = []
        for item in items:
            product = item.product
            product_id = product.product_id
            product_name = product.product_name
            product_url = product.product_image_url
            product_price = product.product_price
            total_product_price = product.product_price * item.quantity
            serialized_item = {
                'product_id': product_id,
                'product_name': product_name,
                'product_url': product_url,
                'product_price': product_price,
                'quantity': item.quantity,
                'total_product_price': total_product_price
            }
            serialized_items.append(serialized_item)

        return serialized_items

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_cart_price(self, obj):
        total_price = sum(item.product.product_price * item.quantity for item in obj.items.all())
        return total_price
