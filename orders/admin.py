from django.contrib import admin

from orders.models import ServiceOrder, ProductOrder, ExpressCalc

admin.site.register(ServiceOrder)
admin.site.register(ProductOrder)
admin.site.register(ExpressCalc)
