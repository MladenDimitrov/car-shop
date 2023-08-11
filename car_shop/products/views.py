from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from car_shop.products.models import Products
from car_shop.products.forms import AddProduct


class ShowProducts(generic.ListView):
    template_name = 'products_page/catalog.html'
    model = Products


@login_required
def product_details(request, **kwargs):
    user = request.user
    more_info = Products.objects.get(pk=kwargs['part_pk'])

    form = AddProduct(instance=more_info)
    form.fields['buyer'].initial = user
    form.fields['product'].initial = more_info
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_page')
    context = {
        'product_details': more_info,
        'form': form
    }
    return render(request, template_name='products_page/product_details_page.html', context=context)
