from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from blog.serializers import ServiceSerializer
from blog.models import Service


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer