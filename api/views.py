from django.shortcuts import render
from rest_framework import viewsets, serializers
from product.models import Product, Category
from . serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
def api_home(requests):
    pass 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    # url = category/{category id}/products
    @action(detail=True,methods=['get'])
    def products(self,request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            products = Product.objects.filter(product_category=category)
            products_serializer = ProductSerializer(products,many=True,context = {'request':request})
            return Response(products_serializer.data)
        except Exception as e:
            return Response({'message': 'Category might not exist. Error'})
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
