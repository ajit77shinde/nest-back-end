from django.shortcuts import render
from rest_framework import viewsets, serializers, status
from product.models import Product, Category, Cart, CartItem
from . serializers import ProductSerializer, CategorySerializer, CartSerializer, CartItemSerializer
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
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            products = Product.objects.filter(product_category=category)
            products_serializer = ProductSerializer(
                products, many=True, context={'request': request})
            return Response(products_serializer.data)
        except Exception as e:
            return Response({'message': 'Category might not exist. Error'})

    # GET /api/category/ - List all categories
    # POST /api/category/ - Create a new category
    # GET /api/category/{pk}/ - Retrieve a specific category
    # PUT /api/category/{pk}/ - Update a specific category
    # DELETE /api/category/{pk}/ - Delete a specific category

    # url - category/
    # @action(detail=True,methods=['get'])

    def list(self, request):
        """
        List all categories
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=True,methods=['post'])
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

# Cart View


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            product = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Invalid product ID'}, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def update_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        try:
            cart_item = CartItem.objects.get(
                cart=cart, product__product_id=product_id)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)

        if quantity is not None:
            cart_item.quantity = quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'])
    def remove_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')

        try:
            cart_item = CartItem.objects.get(
                cart=cart, product__product_id=product_id)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
