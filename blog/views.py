from rest_framework.generics import ListAPIView, RetrieveAPIView


from blog.serializers import ServiceSerializer, CaseSerializer, PostSerializer, PriceItemSerializer
from blog.models import Service, Case, Post, PriceItem


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailView(RetrieveAPIView):
    lookup_field = 'slug'
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


class ServicePricesListView(ListAPIView):
    queryset = PriceItem.objects.all()
    serializer_class = PriceItemSerializer