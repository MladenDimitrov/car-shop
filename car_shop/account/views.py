from django.shortcuts import render, redirect
from car_shop.account.forms import RegisterForm, LoginForm
# Create your views here.


def profile_page(request):
    return render(request, template_name='account/profile_page.html')


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login_page')
    context = {
        'form': form,
    }
    return render(request, template_name='account/register_page.html', context=context)


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, template_name='account/login_page.html', context=context)


def edit_profile(request):
    return render(request, template_name='account/edit_profile_page.html')
