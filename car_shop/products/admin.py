from django.contrib import admin
from car_shop.products.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['category_of_product', 'type_of_product', 'manufacturer', 'batch_number', 'price']
    list_filter = ['category_of_product', 'manufacturer']
    fields = [
        'image_of_the_product',
        ('for_car', 'engine'),
        ('manufacturer', 'batch_number'),
        'specifications',
        ('category_of_product', 'type_of_product', 'price')
    ]
