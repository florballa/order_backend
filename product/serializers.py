from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    categories = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'default_price', 'description', 'categories']

    def get_categories(self, product):
        return ','.join(product.categories.values_list('name', flat=True))


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'default_price', 'description', 'categories']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']
