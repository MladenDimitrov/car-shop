from django.urls import path
from car_shop.account import views
from car_shop.account.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path('profile/', views.profile_page, name='profile_page'),
    path('register/', RegisterUserView.as_view(), name='register_page'),
    path('login/', LoginUserView.as_view(), name='login_page'),
    path('logout/', LogoutUserView.as_view(), name='logout_page'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('order_details/', views.order_details, name='details_for_orders')
]
