from rest_framework.generics import CreateAPIView

from orders.models import ServiceOrder, ProductOrder
from orders.serializers import ServiceOrderSerializer, ProductOrderSerializer


class ServiceOrderCreateView(CreateAPIView):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer


class ProductOrderCreateView(CreateAPIView):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer