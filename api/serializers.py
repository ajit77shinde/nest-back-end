from rest_framework import serializers
from product.models import Product , Category,Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__" # else sepcified field add in ['field name']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__" # else sepcified field add in ['field name']
class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Cart
        #fields = "__all__" # else sepcified field add in ['field name']
        fields = ('cart_id','product','quantity','user_id')