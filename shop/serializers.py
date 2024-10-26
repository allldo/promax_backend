from django.db.models import Model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from shop.models import Product, Category, SubCategory, Image


class ProductSerializer(ModelSerializer):
    images = SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]

class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'title')


class CategorySerializer(ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields =('id', 'title', 'sub_categories')
