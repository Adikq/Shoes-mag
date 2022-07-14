from django.contrib import admin
from .models import ShoesCategory, Shoes, ShoesSize, Order, ShoesPhoto


class OrderInlines(admin.TabularInline):
    model = Order
    extra = 1
    readonly_fields = ('name', 'number', 'address')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('shoes', 'name', 'number', 'address')
    readonly_fields = ('shoes', 'name', 'number', 'address')

@admin.register(Shoes)
class Shoes(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ShoesPhoto)
admin.site.register(ShoesSize)
admin.site.register(ShoesCategory)