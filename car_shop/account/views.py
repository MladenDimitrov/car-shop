from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import mixins as auth_mixins
from car_shop.account.forms import RegisterUserForm, ProfileDetails
from django.urls import reverse_lazy
from django.views import generic as views
from car_shop.account.models import AppUser
from car_shop.common.models import Person


class RegisterUserView(views.CreateView):
    template_name = 'account/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_page')


class LoginUserView(auth_views.LoginView):
    template_name = 'account/login_page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


@login_required
def edit_profile(request):
    auth_username = request.user
    print(auth_username)
    check_for_personal_info = True
    try:
        user_info = Person.objects.get(user=auth_username)
    except:
        form = ProfileDetails()
        check_for_personal_info = False
        print('entered the except block')

    else:
        print('hello')
        form = ProfileDetails(instance=user_info)

    form.fields['user'].initial = auth_username
    if request.method == 'POST':
        if check_for_personal_info:
            print('first')
            print(check_for_personal_info)
            user_info = Person.objects.get(user=auth_username)
            form = ProfileDetails(request.POST, request.FILES, instance=user_info)
            if form.is_valid():
                print(form.is_valid())
                print('final')
                print(check_for_personal_info)
                form.save()
                print(form.save)
        else:
            print('second')
            print(check_for_personal_info)
            form = ProfileDetails(request.POST, request.FILES)
            # print(form)
            # print(form.save())
            print(form.is_valid())
            if form.is_valid():
                print(form.is_valid())
                print('final')
                print(check_for_personal_info)
                form.save()
                print(form.save)

    context = {
        'form': form,
    }
    return render(request, template_name='account/edit_profile_page.html', context=context)


@login_required()
def profile_page(request):
    auth_user = request.user
    context = {}
    print(auth_user)
    try:
        user_info = Person.objects.get(user=auth_user)
    except:
        return redirect(to='edit_profile')
    else:
        context['user_info'] = user_info
        print('else')

    return render(request, template_name='account/profile_page.html', context=context)
