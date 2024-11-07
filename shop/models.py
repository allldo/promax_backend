from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, SET_NULL, CASCADE, JSONField, \
    TextField, ImageField, ManyToManyField, SlugField
from pytils.translit import slugify

class Product(Model):
    title = CharField(max_length=225)
    slug = SlugField(max_length=275, unique=True, blank=True)
    artikul = IntegerField()
    description = TextField(null=True, blank=True)
    sposob_ukladki = TextField(null=True, blank=True)
    parketnaya_himia = TextField(null=True, blank=True)
    sub_category = ForeignKey("SubCategory", on_delete=SET_NULL, null=True)
    price = IntegerField()
    sale = IntegerField(default=0)
    # {"width": "123", "length": "53"} такого вида (str)
    size = JSONField()
    chars = JSONField()
    detail_chars = JSONField()
    images = ManyToManyField("Image", blank=True)
    is_trend = BooleanField(default=False)
    is_hit = BooleanField(default=False)
    is_best = BooleanField(default=False)
    sale_price = IntegerField(null=True, blank=True)
    useful_product = ManyToManyField("shop.Product", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.sale_price = self.price
        if self.sale != 0:
            self.sale_price = self.price * (1 - self.sale / 100)
        super(Product, self).save(*args, **kwargs)

    def get_discounted_price(self):
        return self.price * (1 - self.sale / 100)

class Category(Model):
    title = CharField(max_length=225)

    def __str__(self):
        return self.title

class SubCategory(Model):
    title = CharField(max_length=225)
    category = ForeignKey("Category", on_delete=CASCADE, related_name="sub_categories")

    def __str__(self):
        return self.title

class Image(Model):
    image = ImageField(upload_to='images')
    def __str__(self):
        return f"Image № {self.id}"

