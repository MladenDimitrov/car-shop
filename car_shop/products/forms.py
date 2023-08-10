from django import forms
from car_shop.common.models import ShoppingCart


class AddProduct(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = '__all__'
