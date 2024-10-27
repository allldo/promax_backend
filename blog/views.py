from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from blog.serializers import ServiceSerializer, CaseSerializer, PostSerializer
from blog.models import Service, Case, Post


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class CasesListView(ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostSerializer