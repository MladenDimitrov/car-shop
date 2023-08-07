from django import forms
from car_shop.common.models import Order


class MakeOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
