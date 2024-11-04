from django.urls import path

from orders.views import ServiceOrderCreateView

urlpatterns = [
    path('service/', ServiceOrderCreateView.as_view()),
]