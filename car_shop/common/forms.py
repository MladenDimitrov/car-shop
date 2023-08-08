from django import forms
from car_shop.common.models import Order, ShoppingCart


class MakeOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ShowItems(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = '__all__'
