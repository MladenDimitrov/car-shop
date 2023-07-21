from django import forms
from car_shop.account.models import Person


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'username',
                    'class': 'username'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'password',
                    'class': 'password'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'email',
                    'class': 'email'
                }
            )

        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'username'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'password'
                }
            )
        }
