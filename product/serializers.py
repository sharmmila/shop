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
        fields = 'product text '.split()



class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'product text '.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()



class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()