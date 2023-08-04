from django.contrib import admin
from car_shop.products.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass
