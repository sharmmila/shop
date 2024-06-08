from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Product, Review, Category
from .serializers import (ProductSerializer, ProductDetailSerializer, ReviewSerializer,
                          ReviewDetailSerializer, CategorySerializer, CategoryDetailSerializer,
                          ProductValidateSerializer, ReviewValidateSerializer, CategoryValidateSerializer)


# @api_view(['GET', 'POST'])
# def products_list_api_view(request):
#     if request.method == 'GET':
#       products = Product.objects.all()
#       list_ = ProductSerializer(products, many=True).data
#       return Response(data=list_, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ProductValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#              return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         price = serializer.validated_data.get('price')
#         categories = serializer.validated_data.get('categories')
#
#         product = Product.objects.create(
#             title=title,
#             description=description,
#             price=price,
#         )
#         product.categories.set(categories)
#         product.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data=ProductDetailSerializer(product).data)
#
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def products_detail_api_view(request, id): # 100
#      try:
#          product = Product.objects.get(id=id)
#      except Product.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND,
#                          data={'error': 'Product not found'})
#      if request.method == 'GET':
#        product_dict = ProductDetailSerializer(product).data
#        return Response(data=product_dict)
#      elif request.method == 'PUT':
#          serializer = ProductValidateSerializer(data=request.data)
#          serializer.is_valid(raise_exception=True)
#          product.title = serializer.validated_data.get('title')
#          product.description = serializer.validated_data.get('description')
#          product.price = serializer.validated_data.get('price')
#          product.categories.set(serializer.validated_data.get('categories'))
#          product.save()
#          return Response(status=status.HTTP_201_CREATED,
#                          data=ProductDetailSerializer(product).data)
#      elif request.method == 'DELETE':
#          try:
#              product.delete()
#          except:
#              return Response(status=status.HTTP_400_BAD_REQUEST,
#                              data={'error': 'Product protected'})
#          return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# @api_view(['GET', 'POST'])
# def categories_list_api_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         products_count = Product.objects.count()
#         list_ = CategorySerializer(categories, many=True).data
#         return Response(data=list_, count=products_count, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         name = serializer.validated_data.get('name')
#         category = Category.objects.create(name=name)
#         category.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data=CategoryDetailSerializer(category).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def categories_detail_api_view(request, id): # 100
#      try:
#          category = Category.objects.get(id=id)
#      except Category.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND,
#                          data={'error': 'Category not found'})
#      if request.method == 'GET':
#          category_dict = CategoryDetailSerializer(category).data
#          return Response(data=category_dict)
#      elif request.method == 'PUT':
#          serializer = CategoryDetailSerializer(data=request.data)
#          serializer.is_valid(raise_exception=True)
#          category.name = serializer.validated_data.get('name')
#          category.save()
#          return Response(status=status.HTTP_201_CREATED,
#                          data=CategoryDetailSerializer(category).data)
#      elif request.method == 'DELETE':
#          try:
#              category.delete()
#          except:
#              return Response(status=status.HTTP_400_BAD_REQUEST,
#                              data={'error': 'Category protected'})
#          return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# @api_view(['GET', 'POST'])
# def reviews_list_api_view(request):
#     if request.method == 'GET':
#        reviews = Review.objects.all()
#        rating = sum(Review.stars)/len(Review.stars)
#        list_ = ReviewSerializer(reviews, many=True).data
#        return Response(data=list_, rating= rating, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         text = serializer.validated_data.get('description')
#         stars = serializer.validated_data.get('stars')
#         product = serializer.validated_data.get('product')
#         review = Review.objects.create(
#             text=text,
#             stars=stars,
#         )
#         review.product = product
#         review.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data=ReviewDetailSerializer(review).data)



#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def reviews_detail_api_view(request, id): # 100
#      try:
#          review = Review.objects.get(id=id)
#      except Review.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND,
#                          data={'error': 'Review not found'})
#      if request.method == 'GET':
#        review_dict = ReviewDetailSerializer(review).data
#        return Response(data=review_dict)
#      elif request.method == 'PUT':
#          serializer = ReviewDetailSerializer(data=request.data)
#          serializer.is_valid(raise_exception=True)
#          review.text = serializer.validated_data.get('text')
#          review.stars = serializer.validated_data.get('stars')
#          review.product = serializer.validated_data.get('product')
#          review.save()
#          return Response(status=status.HTTP_201_CREATED,
#                          data=ReviewDetailSerializer(review).data)
#      elif request.method == 'DELETE':
#          try:
#              review.delete()
#          except:
#              return Response(status=status.HTTP_400_BAD_REQUEST,
#                              data={'error': 'Review protected'})
#          return Response(status=status.HTTP_204_NO_CONTENT)



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        list_ = ProductSerializer(products, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        categories = serializer.validated_data.get('categories')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
        )
        product.categories.set(categories)
        product.save()
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)



class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance.title = serializer.validated_data.get('title')
        instance.description = serializer.validated_data.get('description')
        instance.price = serializer.validated_data.get('price')
        instance.categories.set(serializer.validated_data.get('categories'))
        instance.save()

        return Response(status=status.HTTP_200_OK, data=ProductDetailSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = self.get_queryset()
        products_count = Product.objects.count()
        list_ = self.get_serializer(categories, many=True).data
        return Response(data={'categories': list_, 'count': products_count}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        name = serializer.validated_data.get('name')
        category = Category.objects.create(name=name)
        category.save()
        return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category).data)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategoryDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance.name = serializer.validated_data.get('name')
        instance.save()

        return Response(status=status.HTTP_200_OK, data=CategoryDetailSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        reviews = self.get_queryset()
        total_stars = sum(review.stars for review in reviews)
        count = reviews.count()
        average_rating = total_stars / count if count > 0 else 0
        list_ = self.get_serializer(reviews, many=True).data
        return Response(data={'reviews': list_, 'rating': average_rating}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        product = serializer.validated_data.get('product')

        review = Review.objects.create(
            text=text,
            stars=stars,
            product=product
        )
        return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(review).data)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReviewDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance.text = serializer.validated_data.get('text')
        instance.stars = serializer.validated_data.get('stars')
        instance.product = serializer.validated_data.get('product')
        instance.save()

        return Response(status=status.HTTP_200_OK, data=ReviewDetailSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
