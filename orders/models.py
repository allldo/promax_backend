from django.db.models import Model, CharField, ForeignKey, EmailField, TextField, SET_NULL, DateTimeField, \
    ManyToManyField


class ServiceOrder(Model):
    name = CharField()
    email = EmailField()
    phone_number = CharField()
    delivery_on_order = TextField()
    comments_on_order = TextField()
    service = ForeignKey("blog.Service", on_delete=SET_NULL, null=True, blank=True)
    price = ForeignKey("blog.Price", on_delete=SET_NULL, null=True, blank=True)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.date}"


class ProductOrder(Model):
    name = CharField()
    email = EmailField()
    phone_number = CharField()
    delivery_on_order = TextField()
    comments_on_order = TextField()
    order_items = ManyToManyField("shop.Product", blank=True)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.date}"