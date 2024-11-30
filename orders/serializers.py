from rest_framework.exceptions import ValidationError
from rest_framework.fields import ListField, DictField, IntegerField
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
            product_items.append(ProductOrderItem.objects.create(product_id=product_id, order=product_order, count=count))
        product_order.order_items.set(product_items)

        return product_order