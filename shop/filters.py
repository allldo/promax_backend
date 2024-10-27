import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    categoryId = django_filters.NumberFilter(field_name='sub_category__category__id', lookup_expr='exact')
    subCategoryId = django_filters.NumberFilter(field_name='sub_category__id', lookup_expr='exact')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []