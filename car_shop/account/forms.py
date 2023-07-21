from django import forms
from car_shop.account.models import Person


class LoginForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'username'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'password'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'email'
                }
            )

        }

