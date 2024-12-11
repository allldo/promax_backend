from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from blog.serializers import ServiceSerializer, CaseSerializer, PostSerializer, PriceItemSerializer, \
    AdvantageSerializer, FloorWorksSerializer, QuestionSerializer
from blog.models import Service, Case, Post, PriceItem, Advantage, FloorWorks, Question
from orders.services import send_email_question


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


class AdvantageListView(ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


class FloorWorksListView(ListAPIView):
    queryset = FloorWorks.objects.all()
    serializer_class = FloorWorksSerializer


class QuestionCreateView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):

        question = serializer.save()
        send_email_question(question, send_to="info@parket-promax.ru")