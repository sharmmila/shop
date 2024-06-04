from rest_framework import serializers
from .models import Product, Review, Category
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = 'id title description price category'.split()


class ProductDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = 'id title description price category'.split()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length= 100, min_length =2)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    category = serializers.ListField(child=serializers.IntegerField(min_value=1), required=False)

    def validate_categories(self, categories):
        categories = list(set(categories))  # 1,2,3
        tags_from_db = [i.id for i in Category.objects.filter(id__in=categories)]
        if len(tags_from_db) != len(categories):
            raise ValidationError('Category does not exist')
        return categories


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'product text stars'.split()



class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'product text stars'.split()

class ReviewValidateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    text = serializers.CharField(required=True)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=False)
    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=self.product_id)
        except:
            raise ValidationError('Product does not exist')
        return product_id


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()



class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
