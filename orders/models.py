from django.db.models import Model, CharField, ForeignKey, EmailField, TextField, SET_NULL, DateTimeField, \
    ManyToManyField


class ServiceOrder(Model):
    name = CharField(verbose_name='Имя')
    email = EmailField(verbose_name='Электронная почта')
    phone_number = CharField(verbose_name='Номер телефона')
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
    name = CharField(verbose_name='Имя')
    email = EmailField(verbose_name='Электронная почта')
    phone_number = CharField(verbose_name='Номер телефона')
    delivery_on_order = TextField(verbose_name='Доставка по заказу')
    comments_on_order = TextField(verbose_name='Комментарии по заказу')
    order_items = ManyToManyField("shop.Product", blank=True, verbose_name='Продукты в заказе')
    date = DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = "Заказ продукта"
        verbose_name_plural = "Заказы продуктов"

    def __str__(self):
        return f"{self.name} {self.date}"