from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, SET_NULL, CASCADE, JSONField, TextField

class Product(Model):
    title = CharField(max_length=225)
    slug = CharField(max_length=225)
    artikul = IntegerField()
    description = TextField()
    sub_category = ForeignKey("SubCategory", on_delete=SET_NULL, null=True)
    price = IntegerField()
    size = JSONField()
    chars = JSONField()
    images = JSONField()
    is_trend = BooleanField(default=False)
    is_hit = BooleanField(default=False)
    is_best = BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(Model):
    title = CharField(max_length=225)

class SubCategory(Model):
    title = CharField(max_length=225)
    category = ForeignKey("Category", on_delete=CASCADE)

# class Service(Model):
#     title
#
