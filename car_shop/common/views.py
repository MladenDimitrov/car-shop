from django.shortcuts import render
# from car_shop.account.models import Person


# Create your views here.


def home_page(request):
    # name = Person.objects.first()

    # context = {
    #     'name': name
    # }
    return render(request, template_name='common/home_page.html')


def contacts(request):
    return render(request, template_name='common/contacts_page.html')
