from rest_framework.generics import CreateAPIView

from orders.models import ServiceOrder
from orders.serializers import ServiceOrderSerializer


class ServiceOrderCreateView(CreateAPIView):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer