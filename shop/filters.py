import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    categoryId = django_filters.NumberFilter(field_name='sub_category__category__id', lookup_expr='exact')
    subCategoryId = django_filters.NumberFilter(field_name='sub_category__id', lookup_expr='exact')
    price_min = django_filters.NumberFilter(field_name='sale_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='sale_price', lookup_expr='lte')

    # hit = django_filters.BooleanFilter(field_name='is_hit', lookup_expr='exact')
    # trend = django_filters.BooleanFilter(field_name='is_trend', lookup_expr='exact')
    # best = django_filters.BooleanFilter(field_name='is_best', lookup_expr='exact')
    filter = django_filters.CharFilter(method='filter_by_unique_flag')
    class Meta:
        model = Product
        fields = []

    def filter_by_unique_flag(self, queryset, name, value):
        if value == 'hit':
            return queryset.filter(is_hit=True)
        elif value == 'trend':
            return queryset.filter(is_trend=True)
        elif value == 'best':
            return queryset.filter(is_best=True)
        return queryset