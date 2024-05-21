from rest_framework import serializers
from .models import Product, Review, Category
from django.db.models import Avg, Count

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = 'id title description price category'.split()


class ProductDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = 'id title description price category'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'product text stars'.split()

        def get_queryset(self):
            return Product.objects.annotate(rating=Avg('reviews__stars'))


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'product text stars'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

        def get_queryset(self):
            return Category.objects.annotate(products_count=Count('product'))


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()