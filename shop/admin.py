from django.contrib import admin

from shop.models import Product, SubCategory, Category, Image

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Image)
