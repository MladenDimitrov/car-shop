from django import forms
from car_shop.common.models import ShoppingCart
from car_shop.products.models import TestModel


class AddProduct(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'
