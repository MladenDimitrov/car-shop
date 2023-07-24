from django.urls import path, include
from car_shop.common import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contacts/', views.contacts, name='contacts_page'),
]
