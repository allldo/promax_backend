from django.contrib import admin

from shop.models import Product, SubCategory, Category, Image, Attachment

admin.site.register(Attachment)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Image)
