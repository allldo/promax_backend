from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from orders.models import ServiceOrder, ProductOrder, ExpressCalc
from orders.serializers import ServiceOrderSerializer, ProductOrderSerializer, ExpressCalcSerializer
from orders.services import send_email_order, send_email_service, send_email_express


class ServiceOrderCreateView(CreateAPIView):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer

    def perform_create(self, serializer):

        service_order = serializer.save()
        send_email_service(service_order, send_to="info@parket-promax.ru")


class ProductOrderCreateView(CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        product_order = serializer.save(user=self.request.user)
        send_email_order(product_order, send_to="info@parket-promax.ru")


class ExpressCalcCreateView(CreateAPIView):
    queryset = ExpressCalc.objects.all()
    serializer_class = ExpressCalcSerializer

    def perform_create(self, serializer):

        express_calc = serializer.save()
        send_email_express(express_calc, send_to="info@parket-promax.ru")
