from django.shortcuts import render, redirect
from car_shop.common.models import Person, ShoppingCart, Order
from car_shop.common.forms import MakeOrder, ShowItems
from django.contrib.auth.decorators import login_required


def home_page(request):
    # user = request.user
    # name = Person.objects.get(user=user)
    # context = {
    #     'name': name
    # }

    return render(request, template_name='common/home_page.html')


def contacts(request):
    return render(request, template_name='common/contacts_page.html')


@login_required
def shopping_cart(request):
    user = request.user
    cart = ShoppingCart.objects.filter(buyer=user).filter(confirm_purchase_of_product=False)
    context = {
        'number_of_items': len(cart),
        'products': cart,
        'user': user
    }
    return render(request, template_name='common/shopping_cart_page.html', context=context)


@login_required
def delete_item(request, **kwargs):
    item = ShoppingCart.objects.get(pk=kwargs['item_pk'])
    form = ShowItems(instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect(to='shopping_cart_page')
    context = {
        'item': item,
        'form': form
    }
    return render(request, template_name='common/delete_item_page.html', context=context)


@login_required
def order(request):
    user = request.user
    cart = ShoppingCart.objects.filter(buyer=user).filter(confirm_purchase_of_product=False)
    total_price = 0
    for product in cart:
        total_price += product.price
    form = MakeOrder()
    form.fields['customer'].initial = user
    form.fields['products'].initial = cart
    form.fields['total_price'].initial = total_price
    if request.method == 'POST':
        form = MakeOrder(request.POST)
        if form.is_valid():
            for item in cart:
                item.confirm_purchase_of_product = not item.confirm_purchase_of_product
                item.save()
            form.save()

    context = {
        'form': form
    }
    return render(request, template_name='common/make_order_page.html', context=context)
