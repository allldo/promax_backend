from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response

from shop.models import Product
from shop.serializers import ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductHitsView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        products = Product.objects.filter(is_hit=True)
        serialized = ProductSerializer(products, many=True)
        return Response({"products_hit": serialized.data}, status=status.HTTP_200_OK)

class ProductTrendView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        products = Product.objects.filter(is_best=True)
        serialized = ProductSerializer(products, many=True)
        return Response({"products_best": serialized.data}, status=status.HTTP_200_OK)

class ProductBestView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        products = Product.objects.filter(is_trend=True)
        serialized = ProductSerializer(products, many=True)
        return Response({"products_trend": serialized.data}, status=status.HTTP_200_OK)