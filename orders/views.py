from rest_framework.generics import CreateAPIView

from orders.models import ServiceOrder, ProductOrder, ExpressCalc
from orders.serializers import ServiceOrderSerializer, ProductOrderSerializer, ExpressCalcSerializer


class ServiceOrderCreateView(CreateAPIView):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer


class ProductOrderCreateView(CreateAPIView):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer


class ExpressCalcCreateView(CreateAPIView):
    queryset = ExpressCalc.objects.all()
    serializer_class = ExpressCalcSerializer