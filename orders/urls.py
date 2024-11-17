from django.urls import path

from orders.views import ServiceOrderCreateView, ProductOrderCreateView, ExpressCalcCreateView

urlpatterns = [
    path('service/', ServiceOrderCreateView.as_view()),
    path('product/', ProductOrderCreateView.as_view()),
    path('express_calc/', ExpressCalcCreateView.as_view()),
]