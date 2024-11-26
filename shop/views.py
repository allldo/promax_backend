from django.db import connection
from django.db.models import Min, Max, FloatField
from django.db.models.fields.json import KeyTextTransform
from django.db.models.functions import Cast
from django.template.context_processors import request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from cabinet.models import CustomUser
from shop.filters import ProductFilter
from shop.models import Product, Category
from shop.serializers import ProductSerializer, CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filterset = self.filterset_class(request.query_params, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs
        width_max = request.query_params.get('width_max', None)
        width_min = request.query_params.get('width_min', None)
        length_max = request.query_params.get('length_max', None)
        length_min = request.query_params.get('length_min', None)

        if width_max is not None or width_min is not None or length_max is not None or length_min is not None:
            queryset = self.filter_products_by_size(queryset, width_max, width_min, length_max, length_min)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def filter_products_by_size(self, queryset, width_max, width_min, length_max, length_min):
        product_ids = list(queryset.values_list('id', flat=True))

        if not product_ids:
            return Product.objects.none()

        with connection.cursor() as cursor:
            query = "SELECT * FROM shop_product WHERE id IN %s"
            params = [tuple(product_ids)]

            if width_max is not None and width_max != 0:
                query += " AND CAST(size->>'width' AS FLOAT) <= %s"
                params.append(float(width_max))
            if width_min is not None and width_min != 0:
                query += " AND CAST(size->>'width' AS FLOAT) >= %s"
                params.append(float(width_min))
            if length_max is not None and length_max != 0:
                query += " AND CAST(size->>'length' AS FLOAT) <= %s"
                params.append(float(length_max))
            if length_min is not None and length_min != 0:
                query += " AND CAST(size->>'length' AS FLOAT) >= %s"
                params.append(float(length_min))

            if self.request.GET.get('is_hit') is not None:
                query += " AND is_hit = %s"
                params.append(self.request.GET.get('is_hit').lower() == 'true')
            if self.request.GET.get('is_trend') is not None:
                query += " AND is_trend = %s"
                params.append(self.request.GET.get('is_trend').lower() == 'true')
            if self.request.GET.get('is_best') is not None:
                query += " AND is_best = %s"
                params.append(self.request.GET.get('is_best').lower() == 'true')

            cursor.execute(query, params)
            product_ids = [row[0] for row in cursor.fetchall()]

        return Product.objects.filter(id__in=product_ids)

class ProductDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductHitsView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        products = Product.objects.filter(is_hit=True)
        serialized = ProductSerializer(products, many=True)
        return Response({"products": serialized.data}, status=status.HTTP_200_OK)

class ProductTrendView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        products = Product.objects.filter(is_trend=True)
        serialized = ProductSerializer(products, many=True)
        return Response({"products": serialized.data}, status=status.HTTP_200_OK)

class ProductBestView(GenericAPIView):
    serializer_class = ProductSerializer
    def get(self, request):
        products = Product.objects.filter(is_best=True)
        serialized = ProductSerializer(products, many=True)
        return Response({"products": serialized.data}, status=status.HTTP_200_OK)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PriceAndSizeView(APIView):

    def get(self, request):
        category_id = request.query_params.get('categoryId')
        sub_category_id = request.query_params.get('subCategoryId')
        products = Product.objects.all()

        if sub_category_id:
            products = products.filter(sub_category_id=sub_category_id)
        elif category_id:
            products = products.filter(sub_category__category_id=category_id)
        discounted_prices = [product.get_discounted_price() for product in products]
        min_price = min(discounted_prices) if discounted_prices else None
        max_price = max(discounted_prices) if discounted_prices else None

        width_stats = products.annotate(
            width=Cast(KeyTextTransform('width', 'size'), FloatField())
        ).aggregate(
            min_width=Min('width'),
            max_width=Max('width')
        )

        length_stats = products.annotate(
            length=Cast(KeyTextTransform('length', 'size'), FloatField())
        ).aggregate(
            min_length=Min('length'),
            max_length=Max('length')
        )
        data = {
            "prices": {
                "min": min_price,
                "max": max_price,
            },
            "width": {
                "min": width_stats['min_width'],
                "max": width_stats['max_width'],
            },
            "length": {
                "min": length_stats['min_length'],
                "max": length_stats['max_length'],
            }
        }
        return Response(data)


class FavoriteAddAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product = Product.objects.get(id=request.data.get('productId'))
        request.user.favorite.add(product)
        return Response({"result": True})


class FavoriteListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = request.user.favorite.all()

        return Response(ProductSerializer(products, many=True).data)


class FavoriteDeleteAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        product = Product.objects.get(id=request.data.get('productId'))
        request.user.favorite.remove(product)

        return Response({"result": True})