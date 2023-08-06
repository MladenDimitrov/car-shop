from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from car_shop.products.models import Products
from car_shop.products.forms import AddProduct, TestForm
# Create your views here.


@login_required
def show_products(request):
    product = Products.objects.all()
    context = {
        'product': product,
        'drivetrain': 1000
    }
    return render(request, template_name='products_page/catalog.html', context=context)


@login_required
def product_details(request, **kwargs):
    user = request.user
    more_info = Products.objects.get(pk=kwargs['part_pk'])

    form = AddProduct(instance=more_info)
    form.fields['buyer'].initial = user
    if request.method == 'POST':
        print('check')
        form = AddProduct(request.POST, request.FILES, instance=more_info)
        # print(form)
        # form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            print(form.is_valid())
            print('checksave')
            form.save()
            print('checkseved')
            print(form.save)
    context = {
        'product_details': more_info,
        'form': form
    }
    return render(request, template_name='products_page/product_details_page.html', context=context)


def test_page(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, template_name='products_page/test_page.html', context=context)