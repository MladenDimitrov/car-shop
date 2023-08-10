from car_shop.products import views
from django.urls import path
from car_shop.products.views import ShowProducts

urlpatterns = [
    path('', ShowProducts.as_view(), name='products_page'),
    path('details/<int:part_pk>', views.product_details, name='product_details')
]
