from django.urls import path
from car_shop.account import views

urlpatterns = [
    path('', views.profile_page, name='profile_page'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('edit_profile/', views.edit_profile, name='edit_profile_page')
]
