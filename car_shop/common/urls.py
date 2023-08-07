from django.urls import path
from car_shop.common import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contacts/', views.contacts, name='contacts_page'),
    path('shoppping_cart/', views.shopping_cart, name='shopping_cart_page'),
    path('order/', views.order, name='make_order_page')
]
