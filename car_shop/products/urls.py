from car_shop.products import views
from django.urls import path

urlpatterns = [
    path('', views.show_products, name='products_page'),
    path('details/<int:part_pk>', views.product_details, name='product_details'),
    path('form/', views.test_page)
]
