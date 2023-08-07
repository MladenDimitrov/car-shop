from django.shortcuts import render
from car_shop.common.models import Person, ShoppingCart, Order
from car_shop.common.forms import MakeOrder
# Create your views here.


def home_page(request):
    # user = request.user
    # name = Person.objects.get(user=user)
    # context = {
    #     'name': name
    # }

    return render(request, template_name='common/home_page.html')


def contacts(request):
    return render(request, template_name='common/contacts_page.html')


def shopping_cart(request):
    user = request.user
    cart = ShoppingCart.objects.filter(buyer=user)
    context = {
        'products': cart
    }

    return render(request, template_name='common/shopping_cart_page.html', context=context)


def order(request):
    user = request.user
    cart = ShoppingCart.objects.filter(buyer=user)
    order = Order.objects.filter(customer=user)
    # total_price = 0
    # for product in cart:
    #     total_price += product.price
    # form = MakeOrder()
    # form.fields['customer'].initial = user
    # form.fields['products'].initial = cart
    # form.fields['total_price'].initial = total_price
    # if request.method == 'POST':
    #     form = MakeOrder(request.POST)
    #     if form.is_valid():
    #         form.save()
    context = {
        'form': order
    }
    return render(request, template_name='common/make_order_page.html', context=context)
