from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review, Category
from .serializers import (ProductSerializer, ProductDetailSerializer, ReviewSerializer,
                          ReviewDetailSerializer, CategorySerializer, CategoryDetailSerializer)


@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
      products = Product.objects.all()
      list_ = ProductSerializer(products, many=True).data
      return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        categories = request.data.get('categories')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
        )
        product.categories.set(categories)
        product.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(product).data)



@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_api_view(request, id): # 100
     try:
         product = Product.objects.get(id=id)
     except Product.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND,
                         data={'error': 'Product not found'})
     if request.method == 'GET':
       product_dict = ProductDetailSerializer(product).data
       return Response(data=product_dict)
     elif request.method == 'PUT':
         product.title = request.data.get('title')
         product.description = request.data.get('description')
         product.price = request.data.get('price')
         product.categories.set(request.data.get('categories'))
         product.save()
         return Response(status=status.HTTP_201_CREATED,
                         data=ProductDetailSerializer(product).data)
     elif request.method == 'DELETE':
         try:
             product.delete()
         except:
             return Response(status=status.HTTP_400_BAD_REQUEST,
                             data={'error': 'Product protected'})
         return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        products_count = Product.objects.count()
        list_ = CategorySerializer(categories, many=True).data
        return Response(data=list_, count=products_count, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        category.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def categories_detail_api_view(request, id): # 100
     try:
         category = Category.objects.get(id=id)
     except Category.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND,
                         data={'error': 'Category not found'})
     if request.method == 'GET':
         category_dict = CategoryDetailSerializer(category).data
         return Response(data=category_dict)
     elif request.method == 'PUT':
         category.name = request.data.get('name')
         category.save()
         return Response(status=status.HTTP_201_CREATED,
                         data=CategoryDetailSerializer(category).data)
     elif request.method == 'DELETE':
         try:
             category.delete()
         except:
             return Response(status=status.HTTP_400_BAD_REQUEST,
                             data={'error': 'Category protected'})
         return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
       reviews = Review.objects.all()
       rating = sum(Review.stars)/len(Review.stars)
       list_ = ReviewSerializer(reviews, many=True).data
       return Response(data=list_, rating= rating, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('description')
        stars = request.data.get('stars')
        product = request.data.get('product')
        review = Review.objects.create(
            text=text,
            stars=stars,
        )
        review.product = product
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(review).data)





@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id): # 100
     try:
         review = Review.objects.get(id=id)
     except Review.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND,
                         data={'error': 'Review not found'})
     if request.method == 'GET':
       review_dict = ReviewDetailSerializer(review).data
       return Response(data=review_dict)
     elif request.method == 'PUT':
         review.text = request.data.get('text')
         review.stars = request.data.get('stars')
         review.product = request.data.get('product')
         review.save()
         return Response(status=status.HTTP_201_CREATED,
                         data=ReviewDetailSerializer(review).data)
     elif request.method == 'DELETE':
         try:
             review.delete()
         except:
             return Response(status=status.HTTP_400_BAD_REQUEST,
                             data={'error': 'Review protected'})
         return Response(status=status.HTTP_204_NO_CONTENT)


