from django.contrib import admin

from blog.models import Service, Youtube, Telegram, Instagram, Post, Block, Case, CaseItem, Price, PriceItem

admin.site.register(Service)
admin.site.register(Post)
admin.site.register(Youtube)
admin.site.register(Telegram)
admin.site.register(Instagram)
admin.site.register(Block)
admin.site.register(Case)
admin.site.register(CaseItem)
admin.site.register(Price)
admin.site.register(PriceItem)