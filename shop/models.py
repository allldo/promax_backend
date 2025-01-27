from email.policy import default

from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, SET_NULL, CASCADE, JSONField, \
    TextField, ImageField, ManyToManyField, SlugField, FloatField, FileField
from pytils.translit import slugify

class Product(Model):
    title = CharField(max_length=225, verbose_name="Название")
    slug = SlugField(max_length=275, unique=True, blank=True, verbose_name="Слаг")
    artikul = IntegerField(verbose_name="Артикул")
    description = TextField(null=True, blank=True, verbose_name="Описание")
    sposob_ukladki = TextField(null=True, blank=True, verbose_name="Способ укладки")
    parketnaya_himia = TextField(null=True, blank=True, verbose_name="Паркетная Химия")
    sub_category = ForeignKey("SubCategory", on_delete=SET_NULL, null=True, verbose_name="ПодКатегория")
    price = IntegerField(default=1, verbose_name="Цена")
    sale = IntegerField(default=0, verbose_name="Скидка")
    squared_metres = FloatField(null=True, blank=True, verbose_name="Количество метров в упаковке")
    volume = JSONField(null=True, blank=True, verbose_name="Объем и цена")
    attachment = ManyToManyField("Attachment", blank=True, verbose_name="Ссылка на файл")
    # {"width": "123", "length": "53"} такого вида (str)
    size = JSONField(null=True, blank=True, verbose_name="Размер")
    chars = JSONField(null=True, blank=True, verbose_name="Описания")
    detail_chars = JSONField(null=True, blank=True, verbose_name="Детали продукта")
    images = ManyToManyField("Image", blank=True, verbose_name="Изображения")
    is_trend = BooleanField(default=False, verbose_name="Тренд")
    is_hit = BooleanField(default=False, verbose_name="Хит")
    is_best = BooleanField(default=False, verbose_name="Лучший")
    sale_price = IntegerField(null=True, blank=True, verbose_name="Цена после скидки")
    useful_product = ManyToManyField("shop.Product", blank=True, verbose_name="Полезные товары")


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

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Attachment(Model):
    title = CharField(max_length=225, null=True, blank=True,verbose_name="Название")
    file = FileField(upload_to="attachments/", null=True, blank=True)


class Category(Model):
    title = CharField(max_length=225, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(Model):
    title = CharField(max_length=225, verbose_name="Название")
    category = ForeignKey("Category", on_delete=CASCADE, related_name="sub_categories", verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ПодКатегория"
        verbose_name_plural = "ПодКатегории"


class Image(Model):
    image = ImageField(upload_to='images', verbose_name="Изображение")
    def __str__(self):
        return f"Image № {self.id}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"