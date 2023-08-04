from django.shortcuts import render
# Create your views here.


def show_products(request):

    context = {
        'drivetrain': 1000
    }
    return render(request, template_name='products_page/catalog.html', context=context)


def product_details(request, **kwargs):
    pass
