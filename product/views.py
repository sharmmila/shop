from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review, Category
from .serializers import (ProductSerializer, ProductDetailSerializer, ReviewSerializer,
                          ReviewDetailSerializer, CategorySerializer, CategoryDetailSerializer)


@api_view(['GET'])
def products_list_api_view(request):
     products = Product.objects.all()
     list_ = ProductSerializer(products, many=True).data
     return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_detail_api_view(request, id): # 100
     try:
         product = Product.objects.get(id=id)
     except Product.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND,
                         data={'error': 'Product not found'})
     product_dict = ProductDetailSerializer(product).data
     return Response(data=product_dict)



@api_view(['GET'])
def categories_list_api_view(request):
     categories = Category.objects.all()
     list_ = CategorySerializer(categories, many=True).data
     return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def categories_detail_api_view(request, id): # 100
     try:
         category = Category.objects.get(id=id)
     except Category.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND,
                         data={'error': 'Category not found'})
     category_dict = CategoryDetailSerializer(category).data
     return Response(data=category_dict)



# @api_view(['GET'])
# def reviews_list_api_view(request):
#      reviews = Review.objects.all()
#      list_ = ReviewSerializer(reviews, many=True).data
#      return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_detail_api_view(request, id): # 100
     try:
         review = Review.objects.get(id=id)
     except Review.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND,
                         data={'error': 'Review not found'})
     review_dict = ReviewDetailSerializer(review).data
     return Response(data=review_dict)


@api_view(['GET'])
def rating_api_view(request):
     reviews = Review.objects.all()
     list_ = ReviewSerializer(reviews, many=True).data
     return Response(data=list_, status=status.HTTP_200_OK)