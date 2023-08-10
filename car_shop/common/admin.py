from django.contrib import admin

from car_shop.common.models import Person, ShoppingCart, Order, TelephoneNumber, AddressModel, EmailModel, WorkingHoursModel


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(TelephoneNumber)
class TelephoneNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(AddressModel)
class AddressModelAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailModel)
class EmailModelAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingHoursModel)
class WorkingHoursModelAdmin(admin.ModelAdmin):
    pass
