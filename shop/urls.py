from django.urls import path

from shop.views import ProductListView, ProductDetailView, ProductHitsView, ProductTrendView, ProductBestView

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('product/<int:product_id>', ProductDetailView.as_view()),
    path('hit', ProductHitsView.as_view()),
    path('trend', ProductTrendView.as_view()),
    path('best', ProductBestView.as_view()),


]