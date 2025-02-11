from django.contrib import admin
from django.db.models import Q
from django.forms import ModelForm

from blog.models import Service, Youtube, Telegram, Instagram, Post, Block, Case, CaseItem, Price, PriceItem, \
    FloorWorks, FloorWorkItem, Advantage, Question, FloorWorksImage

# admin.site.register(Service)
admin.site.register(Post)
admin.site.register(Youtube)
admin.site.register(Telegram)
admin.site.register(Instagram)
# admin.site.register(Block)
admin.site.register(Case)
# admin.site.register(CaseItem)
# admin.site.register(Price)
# admin.site.register(PriceItem)
admin.site.register(FloorWorks)
# admin.site.register(FloorWorkItem)
admin.site.register(Advantage)
admin.site.register(Question)
@admin.register(FloorWorkItem)
class FloorWorkItemAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(PriceItem)
class PriceItemAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(CaseItem)
class CaseItemAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class PriceInline(admin.TabularInline):
    model = Price.items.through
    extra = 1


class ServiceInline(admin.TabularInline):
    model = Service.blocks.through
    extra = 1


class ServiceAdminForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['blocks'].queryset = Block.objects.filter(
                Q(service=self.instance) | Q(service=None)
            ).distinct()
        else:
            self.fields['blocks'].queryset = Block.objects.filter(service=None)

class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    inlines = [ServiceInline]
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "blocks":
            obj_id = request.resolver_match.kwargs.get('object_id') or request.resolver_match.kwargs.get('pk')

            if obj_id:
                kwargs["queryset"] = Block.objects.filter(service__isnull=True) | Block.objects.filter(
                    service=obj_id)
            else:
                kwargs["queryset"] = Block.objects.filter(service__isnull=True)

        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Service, ServiceAdmin)


class PriceAdmin(admin.ModelAdmin):
    inlines = [PriceInline]
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "items":
            obj_id = request.resolver_match.kwargs.get('object_id') or request.resolver_match.kwargs.get('pk')

            if obj_id:
                kwargs["queryset"] = PriceItem.objects.filter(price_items__isnull=True) | PriceItem.objects.filter(
                    price_items=obj_id)
            else:
                kwargs["queryset"] = PriceItem.objects.filter(price_items__isnull=True)

        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Price, PriceAdmin)

@admin.register(FloorWorksImage)
class FloorWorksImageAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False