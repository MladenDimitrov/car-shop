from django.urls import path
from car_shop.common import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contacts/', views.contacts, name='contacts_page'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart_page'),
    path('delete_item/<int:item_pk>/', views.delete_item, name='delete_item'),
    path('order/', views.order, name='make_order_page')
]
