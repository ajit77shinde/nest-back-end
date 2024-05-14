from django.shortcuts import render
from rest_framework import viewsets, serializers, status
from product.models import Product, Category
from . serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404

# Create your views here.
def api_home(requests):
    pass 

# Category View
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    
    # url = category/{category id}/products
    # This is to get products of a category
    @action(detail=True,methods=['get'])
    def products(self,request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            products = Product.objects.filter(product_category=category)
            products_serializer = ProductSerializer(products,many=True,context = {'request':request})
            return Response(products_serializer.data)
        except Exception as e:
            return Response({'message': 'Category might not exist. Error'})
        


    # GET /api/category/ - List all categories
    # POST /api/category/ - Create a new category
    # GET /api/category/{pk}/ - Retrieve a specific category
    # PUT /api/category/{pk}/ - Update a specific category
    # DELETE /api/category/{pk}/ - Delete a specific category    



    #url - category/
    #@action(detail=True,methods=['get'])
    def list(self, request):
        """
        List all categories
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    #@action(detail=True,methods=['post'])
    def create(self, request):
        """
        Create a new category
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific category
        """
        queryset = self.get_queryset()
        category = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(category)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """                                                                                                         
        Update a specific category
        """
        queryset = self.get_queryset()
        category = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Delete a specific category
        """
        queryset = self.get_queryset()
        category = get_object_or_404(queryset, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
    
    
    
    
    
    
    
    
    
    
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 
    def list(self, request):
        """
        List all products
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def create_data(self, request):
        """
        Create a new product
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def retrieve(self, request, pk=None):
        """
        Retrieve a specific product
        """
        queryset = self.get_queryset()
        product = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(product)
        return Response(serializer.data)
 
    def update(self, request, pk=None):
        """                                                                                                         
        Update a specific product
        """
        queryset = self.get_queryset()
        product = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk=None):
        """
        Delete a specific product
        """
        queryset = self.get_queryset()
        product = get_object_or_404(queryset, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
