from django.core.exceptions import ValidationError


def check_name(value):
    if not value.isalpha():
        raise ValidationError("Your name must start with a letter!")
