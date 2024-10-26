from django.db.models import Model, CharField, SlugField, ImageField
from django.utils.text import slugify


class Post(Model):
    title = CharField(max_length=225)
    #review
    # body = model здесь поле для заполнения
    def __str__(self):
        return self.title


class Case(Model):
    title = CharField(max_length=225)
    link = CharField(max_length=325)

    def __str__(self):
        return self.title


class Service(Model):
    title = CharField(max_length=225)
    slug = SlugField(unique=True, blank=True)
    icon = ImageField(upload_to='service_icons/')
    image = ImageField(upload_to='service_images/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)