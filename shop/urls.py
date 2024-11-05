from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import ProductListView, ProductDetailView, ProductHitsView, ProductTrendView, ProductBestView, \
    CategoryListView, PriceAndSizeView, FavoriteAddAPIView, FavoriteListAPIView, FavoriteDeleteAPIView


urlpatterns = [
    path('products', ProductListView.as_view()),
    path('product/<str:slug>', ProductDetailView.as_view()),
    path('hit', ProductHitsView.as_view()),
    path('trend', ProductTrendView.as_view()),
    path('best', ProductBestView.as_view()),

    path('favorite-add', FavoriteAddAPIView.as_view()),
    path('favorite-get', FavoriteListAPIView.as_view()),
    path('favorite-delete', FavoriteDeleteAPIView.as_view()),
    path('categories-list', CategoryListView.as_view()),
    path('prices-and-sizes', PriceAndSizeView.as_view())
]