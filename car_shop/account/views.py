from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from car_shop.account.forms import RegisterUserForm, ProfileDetails
from django.urls import reverse_lazy
from django.views import generic as views
from car_shop.common.models import Person, Order


class RegisterUserView(views.CreateView):
    template_name = 'account/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_page')


class LoginUserView(auth_views.LoginView):
    template_name = 'account/enter_the_matrix.html'


class LogoutUserView(auth_views.LogoutView):
    pass


@login_required
def edit_profile(request):
    auth_username = request.user
    check_for_personal_info = True
    try:
        user_info = Person.objects.get(user=auth_username)
    except:
        form = ProfileDetails()
        check_for_personal_info = False
    else:
        form = ProfileDetails(instance=user_info)

    form.fields['user'].initial = auth_username
    if request.method == 'POST':
        if check_for_personal_info:
            user_info = Person.objects.get(user=auth_username)
            form = ProfileDetails(request.POST, request.FILES, instance=user_info)
            if form.is_valid():
                form.save()
                return redirect(to='profile_page')

        else:
            form = ProfileDetails(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(to='profile_page')
    context = {
        'form': form,
    }
    return render(request, template_name='account/edit_profile_page.html', context=context)


@login_required()
def profile_page(request):
    auth_user = request.user
    context = {}

    try:
        user_info = Person.objects.get(user=auth_user)
    except:
        return redirect(to='edit_profile')
    else:
        context['person'] = user_info

    return render(request, template_name='account/profile_page.html', context=context)


def order_details(request):
    user = request.user
    orders = Order.objects.filter(customer=user)
    context = {
        'order': orders
    }
    return render(request, template_name='account/order_details_page.html', context=context)
