from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from orders.models import ServiceOrder, ProductOrder, ExpressCalc
from orders.serializers import ServiceOrderSerializer, ProductOrderSerializer, ExpressCalcSerializer


class ServiceOrderCreateView(CreateAPIView):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer


class ProductOrderCreateView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    permission_classes = [IsAuthenticated]


class ExpressCalcCreateView(CreateAPIView):
    queryset = ExpressCalc.objects.all()
    serializer_class = ExpressCalcSerializer