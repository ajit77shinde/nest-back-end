from rest_framework import serializers
from product.models import Product , Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__" # else sepcified field add in ['field name']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__" # else sepcified field add in ['field name']