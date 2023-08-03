from django.shortcuts import render
from car_shop.products.models import DriveTrainSemiAxleBox
# Create your views here.


def show_products(request):
    drivetrain = DriveTrainSemiAxleBox.objects.all()
    context = {
        'drivetrain': drivetrain
    }
    return render(request, template_name='products_page/catalog.html', context=context)
