from car_shop.products import views
from django.urls import path

urlpatterns = [
    path('', views.show_products, name='products_page'),
    path('details/', views.product_details, name='product_details')
]
