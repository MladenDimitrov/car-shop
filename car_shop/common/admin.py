from django.contrib import admin

from car_shop.common.models import Person, ShoppingCart, Order, TelephoneNumber, AddressModel, EmailModel, \
    WorkingHoursModel


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'user']
    search_fields = ['name', 'email']
    fields = [
        ('name', 'last_name', 'profile_photo'),
        ('email', 'phone_number', 'address'),
        'user'
    ]


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'confirm_purchase_of_product', 'price']
    list_filter = ['confirm_purchase_of_product', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'first_name', 'status', 'phone_number', 'total_price']
    list_filter = ['status']
    search_fields = ['first_name', 'phone_number']
    fields = [
        ('products', 'customer'),
        ('first_name', 'last_name', 'total_price'),
        ('phone_number', 'address'),
        'status'
    ]


@admin.register(TelephoneNumber)
class TelephoneNumberAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'description']


@admin.register(AddressModel)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['address']


@admin.register(EmailModel)
class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'description']


@admin.register(WorkingHoursModel)
class WorkingHoursModelAdmin(admin.ModelAdmin):
    list_display = ['working_days', 'days_off']
