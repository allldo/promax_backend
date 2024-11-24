from django.db.models import Model, CharField, ForeignKey, EmailField, TextField, SET_NULL, DateTimeField, \
    ManyToManyField, PositiveIntegerField, CASCADE, ImageField

from cabinet.models import CustomUser
from shop.models import Product


class ServiceOrder(Model):
    name = CharField(max_length=255, verbose_name='Имя')
    email = EmailField(verbose_name='Электронная почта')
    phone_number = CharField(max_length=255, verbose_name='Номер телефона')
    delivery_on_order = TextField(verbose_name='Доставка по заказу')
    comments_on_order = TextField(verbose_name='Комментарии по заказу')
    service = ForeignKey("blog.Service", on_delete=SET_NULL, null=True, blank=True, verbose_name='Услуга')
    price = ForeignKey("blog.Price", on_delete=SET_NULL, null=True, blank=True, verbose_name='Цена')
    date = DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f"{self.name} {self.date}"

    class Meta:
        verbose_name = "Заказ услуги"
        verbose_name_plural = "Заказы услуг"


class ProductOrder(Model):
    name = CharField(max_length=255, verbose_name='Имя')
    email = EmailField(verbose_name='Электронная почта')
    phone_number = CharField(max_length=255, verbose_name='Номер телефона')
    lift = CharField(max_length=255, verbose_name='Подъем')
    delivery_on_order = TextField(verbose_name='Доставка по заказу')
    comments_on_order = TextField(verbose_name='Комментарии по заказу')
    order_items = ManyToManyField("shop.Product", blank=True, verbose_name='Продукты в заказе')
    date = DateTimeField(auto_now_add=True, verbose_name='Дата')
    user = ForeignKey("cabinet.CustomUser", on_delete=SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Заказ продукта"
        verbose_name_plural = "Заказы продуктов"

    def __str__(self):
        return f"{self.name} {self.date}"


class ProductOrderItem(Model):
    order = ForeignKey(ProductOrder, on_delete=CASCADE, related_name="items", verbose_name='Заказ')
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name='Продукт')
    count = PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.product} x {self.count}"


class ExpressCalc(Model):
    name = CharField(max_length=255, verbose_name="Имя")
    squared_metres = PositiveIntegerField(verbose_name="Площадь помещения")
    parquet_age = PositiveIntegerField(verbose_name="Возраст паркета")
    phone_number = CharField(max_length=255, verbose_name="Номер телефона")
    photo = ImageField(upload_to="ExpressCalcPhotos/", verbose_name="Фото")

    class Meta:
        verbose_name = "Расчет"
        verbose_name_plural = "Расчеты"