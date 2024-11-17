from rest_framework.exceptions import ValidationError
from rest_framework.fields import ListField, DictField, IntegerField
from rest_framework.serializers import ModelSerializer

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
        fields = '__all__'

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

        order_items = validated_data.pop('order_items', [])
        product_order = ProductOrder.objects.create(**validated_data)


        for item in order_items:
            product_id = item['id']
            count = item['count']
            ProductOrderItem.objects.create(product_id=product_id, order=product_order, count=count)

        return product_order