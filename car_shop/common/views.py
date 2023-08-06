from django.shortcuts import render
from car_shop.common.models import Person


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
