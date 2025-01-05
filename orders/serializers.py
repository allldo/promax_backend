from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ListField, DictField, IntegerField, CharField, ImageField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from blog.models import PriceItem
from orders.models import ServiceOrder, ProductOrder, ProductOrderItem, ExpressCalc


class ServiceOrderSerializer(ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = '__all__'


class ExpressCalcSerializer(ModelSerializer):
    class Meta:
        model = ExpressCalc
        fields = '__all__'


class ProductOrderSerializer(ModelSerializer):

    order_items = ListField(
        child=DictField(child=IntegerField()),
        write_only=True,
        required=True,
        help_text="Список товаров с id и количеством",
    )

    class Meta:
        model = ProductOrder    
        exclude = ['user']

    def validate_order_items(self, value):

        for item in value:
            if 'id' not in item or 'count' not in item:
                raise ValidationError("Каждый элемент должен содержать 'id' и 'count'.")
            if not isinstance(item['id'], int) or not isinstance(item['count'], int):
                raise ValidationError("'id' и 'count' должны быть целыми числами.")
            if item['count'] <= 0:
                raise ValidationError("'count' должен быть больше нуля.")
            if item['volume'] <= 0:
                raise ValidationError("'volume' должен быть больше нуля.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        order_items = validated_data.pop('order_items', [])
        product_order = ProductOrder.objects.create(**validated_data)
        product_order.user = user
        product_order.save()
        product_items = []
        for item in order_items:
            product_id = item['id']
            count = item['count']
            volume = item['volume']
            product_items.append(ProductOrderItem.objects.create(product_id=product_id, order=product_order, count=count, volume=volume))
        product_order.order_items.set(product_items)

        return product_order


class OrderItemSerializer(ModelSerializer):
    product_id = IntegerField(source='product.id')
    title = CharField(source='product.title')
    sub_category = CharField(source='product.sub_category.title')
    images = SerializerMethodField()

    class Meta:
        model = ProductOrderItem
        fields = ['product_id', 'title', 'sub_category', 'images', 'count']

    def get_images(self, obj):
        return [f"{settings.SERVER_ADDRESS}{image.image.url}" for image in obj.product.images.all()]


class OrderSerializer(ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total_packages = SerializerMethodField()
    total_square_meters = SerializerMethodField()
    total_sum = SerializerMethodField()

    class Meta:
        model = ProductOrder
        fields = ['id', 'date', 'order_items', 'total_square_meters', 'total_packages', 'total_sum']

    def get_total_packages(self, obj):
        return sum(item.count for item in obj.order_items.all())

    def get_total_square_meters(self, obj):
        return sum(item.product.squared_metres * item.count if item.product.squared_metres else 1 for item in obj.order_items.all())

    def get_total_sum(self, obj):
        return obj.total_sum()