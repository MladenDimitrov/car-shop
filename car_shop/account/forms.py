from django import forms
# from car_shop.account.models import Person
from django.contrib.auth import forms as auth_forms, get_user_model, password_validation
from django.utils.translation import gettext_lazy as _
#
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ['username', 'password', 'email']
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={
#                     'placeholder': 'username',
#                     'class': 'username'
#                 }
#             ),
#             'password': forms.PasswordInput(
#                 attrs={
#                     'placeholder': 'password',
#                     'class': 'password'
#                 }
#             ),
#             'email': forms.TextInput(
#                 attrs={
#                     'placeholder': 'email',
#                     'class': 'email'
#                 }
#             )
#
#         }
#
#
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={
#                     'placeholder': 'username',
#                     'class': 'form-control random'
#                 }
#             ),
#             'password': forms.TextInput(
#                 attrs={
#                     'placeholder': 'password',
#                     'class': 'form-control random'
#                 }
#             )
#         }
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(auth_forms.UserCreationForm):
        model = UserModel
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username'
                }
            ),
        }
