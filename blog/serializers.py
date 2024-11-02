from rest_framework.serializers import ModelSerializer

from blog.models import Service, Case, Post, CaseItem, Youtube, Telegram, Instagram, Block, PriceItem, Price


class PriceItemSerializer(ModelSerializer):
    class Meta:
        model = PriceItem
        fields = "__all__"

class PriceSerializer(ModelSerializer):
    items = PriceItemSerializer(many=True)
    class Meta:
        model = Price
        fields = "__all__"

class ServiceSerializer(ModelSerializer):
    prices = PriceSerializer(many=False)
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


class BlockSerializer(ModelSerializer):

    class Meta:
        model = Block
        fields = "__all__"


class PostSerializer(ModelSerializer):
    blocks = BlockSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
