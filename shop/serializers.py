from rest_framework.fields import SerializerMethodField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from django.conf import settings

from shop.models import Product, Category, SubCategory, Image, Attachment


class SubCategorySerializer(ModelSerializer):
    category = StringRelatedField(read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'title', 'category')


class CategorySerializer(ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields =('id', 'title', 'sub_categories')


class ProductNestedSerializer(ModelSerializer):
    images = SerializerMethodField()
    price = SerializerMethodField()
    sub_category = SubCategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ['id', 'slug', 'images', 'price','squared_metres', 'sub_category']

    def get_images(self, obj):
        return [f"{settings.SERVER_ADDRESS}{image.image.url}" for image in obj.images.all()]

    def get_price(self, obj):
        return obj.sale_price


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    images = SerializerMethodField()
    price = SerializerMethodField()
    width = SerializerMethodField()
    length =SerializerMethodField()
    sub_category = SubCategorySerializer(many=False)
    useful_product = ProductNestedSerializer(many=True)
    attachment = AttachmentSerializer(many=True)

    class Meta:
        model = Product
        exclude = ['sale_price']

    def get_images(self, obj):
        return [f"{settings.SERVER_ADDRESS}{image.image.url}" for image in obj.images.all()]

    def get_price(self, obj):
        return obj.sale_price

    def get_width(self, obj):
        size_data = obj.size
        try:
            return float(size_data.get('width'))
        except:
            return None
    #
    def get_length(self, obj):
        size_data = obj.size
        try:
            return size_data.get('length')
        except:
            return None

