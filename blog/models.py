from django.db.models import Model, CharField, SlugField, ImageField, ForeignKey, SET_NULL, ManyToManyField, TextField, \
    IntegerField, EmailField, DateTimeField
from pytils.translit import slugify

from shop.models import Image


class Post(Model):
    title = CharField(max_length=225, verbose_name="Название")
    image = ImageField(upload_to='blog/', verbose_name="Изображение")
    slug = SlugField(max_length=275, unique=True, blank=True, verbose_name="Слаг")
    blocks = ManyToManyField("Block", blank=True, verbose_name="Блоки")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Block(Model):
    image = ImageField(upload_to='blocks/', null=True, blank=True, verbose_name="Изображение")
    title = CharField(max_length=335,null=True, blank=True, verbose_name="Название")
    text = TextField(null=True, blank=True, verbose_name="Текст")
    video = TextField(blank=True)

    def __str__(self):
        return self.title if self.title else f"{self.id}"

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"


class Case(Model):
    youtube = ForeignKey("Youtube", on_delete=SET_NULL, null=True, blank=True, verbose_name="Ютуб")
    tg = ForeignKey("Telegram", on_delete=SET_NULL, null=True, blank=True, verbose_name="Телеграм")
    inst = ForeignKey("Instagram", on_delete=SET_NULL, null=True, blank=True, verbose_name="Инстаграм")

    def __str__(self):
        return f"Case № {self.id}"

    class Meta:
        verbose_name = "Общий кейс"
        verbose_name_plural = "Общий кейс"


class Youtube(Model):
    title = CharField(max_length=225, verbose_name="Название")
    link = CharField(max_length=325, verbose_name="Ссылка")
    items = ManyToManyField("CaseItem", blank=True, verbose_name="Кейсы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ютуб"
        verbose_name_plural = "Ютуб"


class Telegram(Model):
    title = CharField(max_length=225, verbose_name="Название")
    link = CharField(max_length=325, verbose_name="Ссылка")
    items = ManyToManyField("CaseItem", blank=True, verbose_name="Кейсы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Телеграм"
        verbose_name_plural = "Телеграм"


class Instagram(Model):
    title = CharField(max_length=225, verbose_name="Название")
    link = CharField(max_length=325, verbose_name="Ссылка")
    items = ManyToManyField("CaseItem", blank=True, verbose_name="Кейсы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Инстаграм"
        verbose_name_plural = "Инстаграм"


class CaseItem(Model):
    iframe = TextField(blank=True)
    title = CharField(max_length=225, verbose_name="Название")
    link = TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"


class Service(Model):
    title = CharField(max_length=225, verbose_name="Название")
    subtitle = CharField(max_length=275, verbose_name="Описание")
    slug = SlugField(max_length=275, unique=True, blank=True, verbose_name="Слаг")
    icon = ImageField(upload_to='service_icons/', verbose_name="Иконка")
    image = ImageField(upload_to='service_images/', verbose_name="Изображение")
    prices = ForeignKey("Price", on_delete=SET_NULL, null=True, blank=True, verbose_name="Цены")
    blocks = ManyToManyField("blog.Block", related_name="service",blank=True, verbose_name="Блоки")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Price(Model):
    title = CharField(max_length=335, verbose_name="Название")
    items = ManyToManyField("PriceItem", blank=True, related_name="price_items", verbose_name="Цены")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"


class PriceItem(Model):
    name = CharField(max_length=335, verbose_name="Имя")
    price = IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Цена услуги"
        verbose_name_plural = "Цены услуг"


class FloorWorks(Model):
    title = CharField(max_length=275, verbose_name="Название")
    subtitle = CharField(max_length=275, verbose_name="Описание")
    items = ManyToManyField("FloorWorkItem", blank=True, verbose_name="Описания")
    images = ManyToManyField("shop.Image", blank=True, verbose_name="Изображения")

    class Meta:
        verbose_name = "Напольные работы"
        verbose_name_plural = "Напольные работы"


class FloorWorkItem(Model):
    name = CharField(max_length=275, verbose_name="Название")

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описание"


class Advantage(Model):
    text = CharField(max_length=275, verbose_name="Текст")
    image = ForeignKey("shop.Image", on_delete=SET_NULL, null=True, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"


class Question(Model):
    name = CharField(max_length=255, verbose_name="ФИО отправителя")
    phone_number = CharField(max_length=45, verbose_name="Номер телефона")
    email = EmailField(verbose_name="Эл почта")
    question = TextField(verbose_name="Вопрос")
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} задает вопрос"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"