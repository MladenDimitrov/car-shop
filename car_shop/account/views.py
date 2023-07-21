from django.shortcuts import render
from car_shop.account.forms import LoginForm
# Create your views here.


def register_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, template_name='account/register_page.html', context=context)