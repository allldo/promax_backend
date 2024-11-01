from django.db.models import Model, CharField, SlugField, ImageField, ForeignKey, SET_NULL, ManyToManyField, TextField, \
    IntegerField
from pytils.translit import slugify

from shop.models import Image


class Post(Model):
    title = CharField(max_length=225)
    image = ImageField(upload_to='blog/')
    slug = SlugField(max_length=275, unique=True, blank=True)
    blocks = ManyToManyField("Block", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Block(Model):
    image = ImageField(upload_to='blocks/', null=True, blank=True)
    title = CharField(max_length=335)
    text = TextField(null=True, blank=True)


class Case(Model):
    youtube = ForeignKey("Youtube", on_delete=SET_NULL, null=True, blank=True)
    tg = ForeignKey("Telegram", on_delete=SET_NULL, null=True, blank=True)
    inst = ForeignKey("Instagram", on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Case № {self.id}"


class Youtube(Model):
    title = CharField(max_length=225)
    link = CharField(max_length=325)
    items = ManyToManyField("CaseItem", blank=True)

    def __str__(self):
        return self.title


class Telegram(Model):
    title = CharField(max_length=225)
    link = CharField(max_length=325)
    items = ManyToManyField("CaseItem", blank=True)

    def __str__(self):
        return self.title


class Instagram(Model):
    title = CharField(max_length=225)
    link = CharField(max_length=325)
    items = ManyToManyField("CaseItem", blank=True)

    def __str__(self):
        return self.title


class CaseItem(Model):
    iframe = TextField()
    title = CharField(max_length=225)

    def __str__(self):
        return self.title


class Service(Model):
    title = CharField(max_length=225)
    subtitle = CharField(max_length=275)
    slug = SlugField(max_length=275, unique=True, blank=True)
    icon = ImageField(upload_to='service_icons/')
    image = ImageField(upload_to='service_images/')
    prices = ForeignKey("Price", on_delete=SET_NULL, null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Price(Model):
    title = CharField(max_length=335)
    items = ManyToManyField("PriceItem", blank=True, related_name="price_items")

    def __str__(self):
        return self.title

class PriceItem(Model):
    name = CharField(max_length=335)
    price = IntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"
