from django.shortcuts import render, redirect
# from car_shop.account.forms import RegisterForm, LoginForm, RegisterUserForm
# Create your views here.
# def profile_page(request):
#     return render(request, template_name='account/profile_page.html')
#
#
# def register_page(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='login_page')
#     context = {
#         'form': form,
#     }
#     return render(request, template_name='account/register_page.html', context=context)
#
#
# def login_page(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form': form
#     }
#     return render(request, template_name='account/login_page.html', context=context)
#
#
# def edit_profile(request):
#     return render(request, template_name='account/edit_profile_page.html')


from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import mixins as auth_mixins
from car_shop.account.forms import RegisterUserForm
from django.urls import reverse_lazy
from django.views import generic as views


class RegisterUserView(views.CreateView):
    template_name = 'account/register_page.html'
    form_class = RegisterUserForm


class LoginUserView(auth_views.LoginView):
    template_name = 'account/login_page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


# @login_required
# def func_view(request):
#     pass


# class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
#     template_name = 'app_auth/users_list.html'


# class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
#     model = UserModel
#     template_name = 'app_auth/users_list.html'

#     # Login URL only for this view:
#     # login_url = 'custom-login/url'
