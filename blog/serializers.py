from django.conf import settings
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from blog.models import Service, Case, Post, CaseItem, Youtube, Telegram, Instagram, Block, PriceItem, Price, \
    FloorWorkItem, FloorWorks, Advantage, Question


class PriceItemSerializer(ModelSerializer):
    class Meta:
        model = PriceItem
        fields = "__all__"

class PriceSerializer(ModelSerializer):
    items = PriceItemSerializer(many=True)
    class Meta:
        model = Price
        fields = "__all__"

class BlockSerializer(ModelSerializer):

    class Meta:
        model = Block
        fields = "__all__"

class ServiceSerializer(ModelSerializer):
    prices = PriceSerializer(many=False)
    blocks = BlockSerializer(many=True)
    class Meta:
        model = Service
        fields = "__all__"


class CaseItemSerializer(ModelSerializer):

    class Meta:
        model = CaseItem
        fields = "__all__"


class YoutubeSerializer(ModelSerializer):
    items = CaseItemSerializer(many=True)

    class Meta:
        model = Youtube
        fields = "__all__"


class TelegramSerializer(ModelSerializer):
    items = CaseItemSerializer(many=True)

    class Meta:
        model = Telegram
        fields = "__all__"


class InstagramSerializer(ModelSerializer):
    items = CaseItemSerializer(many=True)

    class Meta:
        model = Instagram
        fields = "__all__"


class CaseSerializer(ModelSerializer):
    youtube = YoutubeSerializer(many=False)
    inst = InstagramSerializer(many=False)
    tg = TelegramSerializer(many=False)

    class Meta:
        model = Case
        fields = "__all__"


class PostSerializer(ModelSerializer):
    blocks = BlockSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['blocks'] = sorted(representation['blocks'], key=lambda x: x['id'])
        return representation


class FloorWorkItemSerializer(ModelSerializer):

    class Meta:
        model = FloorWorkItem
        fields = "__all__"


class FloorWorksSerializer(ModelSerializer):

    items = FloorWorkItemSerializer(many=True)
    images = SerializerMethodField()

    class Meta:
        model = FloorWorks
        fields = "__all__"

    def get_images(self, obj):
        return [f"{settings.SERVER_ADDRESS}{image.image.url}" for image in obj.images.all()]


class AdvantageSerializer(ModelSerializer):
    image = SerializerMethodField()
    class Meta:
        model = Advantage
        fields = "__all__"

    def get_image(self, obj):
        if obj.image:
            return f"{settings.SERVER_ADDRESS}{obj.image.image.url}"


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
