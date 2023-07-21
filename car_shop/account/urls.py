from django.urls import path, include
from car_shop.account import views

urlpatterns = [
    path('register/', views.register_page, name='register_page'),
]
