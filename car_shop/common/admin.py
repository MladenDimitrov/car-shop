from django.contrib import admin

from car_shop.common.models import Person, ShoppingCart, Order


# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
