from decimal import Decimal

from django.db.models import Model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from shop.models import Product, Category, SubCategory, Image


class ProductSerializer(ModelSerializer):
    images = SerializerMethodField()
    price = SerializerMethodField()
    width = SerializerMethodField()
    length =SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_images(self, obj):
        return [f"{settings.SERVER_ADDRESS}{image.image.url}" for image in obj.images.all()]

    def get_price(self, obj):
        return float(obj.price * (1 - (obj.sale / 100)))

    def get_width(self, obj):
        size_data = obj.size
        return float(size_data.get('width'))
    #
    def get_length(self, obj):
        size_data = obj.size
        return size_data.get('length')


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'title')


class CategorySerializer(ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields =('id', 'title', 'sub_categories')
