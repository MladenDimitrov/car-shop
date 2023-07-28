from django.urls import path
from car_shop.account import views
from car_shop.account.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    # path('', , name='profile_page'),
    path('register/', RegisterUserView.as_view(), name='register_page'),
    path('login/', LoginUserView.as_view(), name='login_page'),
    path('logout/', LogoutUserView.as_view(), name='logout_page'),
    # path('profile/', ProfileUserView.as_view(), name='profile_page'),
    path('profile/', views.profile_page, name='profile_page')
]
