from django.shortcuts import render
from rest_framework import viewsets
from product.models import Product 
from . serializers import ProductSerializer

# Create your views here.
def api_home(requests):
    pass 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer