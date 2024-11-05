from rest_framework.serializers import ModelSerializer

from orders.models import ServiceOrder, ProductOrder


class ServiceOrderSerializer(ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = '__all__'


class ProductOrderSerializer(ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'