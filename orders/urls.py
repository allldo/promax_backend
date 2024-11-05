from django.urls import path

from orders.views import ServiceOrderCreateView, ProductOrderCreateView

urlpatterns = [
    path('service/', ServiceOrderCreateView.as_view()),
    path('product/', ProductOrderCreateView.as_view()),
]