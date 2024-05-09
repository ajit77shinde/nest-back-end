from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__" # else sepcified field add in ['field name']
        