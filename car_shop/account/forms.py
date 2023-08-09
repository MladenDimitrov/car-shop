from django import forms
from django.contrib.auth import forms as auth_forms, password_validation, get_user_model
from django.utils.translation import gettext_lazy as _
from car_shop.common.models import Person

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat password"}),
        strip=False,
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


class ProfileDetails(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
