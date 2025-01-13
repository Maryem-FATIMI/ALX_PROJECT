from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Wishlist, Review
from .serializers import CategorySerializer, ProductSerializer, WishlistSerializer, ReviewSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import UserAccess
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UserAccess]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #authentication_classes = [TokenAuthentication]
   # permission_classes = [IsAuthenticated, UserAccess]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'stock_quantity']
    search_fields = ['name', 'category__name']  # Allow partial search by name or category
    ordering_fields = ['price', 'stock_quantity', 'created_date']

    @action(detail=True, methods=['post'])
    def reduce_stock(self, request, pk=None):
        product = self.get_object()
        quantity = int(request.data.get('quantity', 0))
        if quantity > product.stock_quantity:
            return Response(
                {"error": "Not enough stock available."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        product.stock_quantity -= quantity
        product.save()
        return Response({"message": "Stock updated successfully."})
    
    @action(detail=True, methods=['get'])
    def product_detail_with_reviews(self, request, pk=None):
        product = self.get_object()
        reviews = Review.objects.filter(product=product)
        product_serializer = ProductSerializer(product)
        review_serializer = ReviewSerializer(reviews, many=True)
        
        return Response({
            'product': product_serializer.data,
            'reviews': review_serializer.data
        })

class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated, UserAccess]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(product=self.kwargs['product_pk'])