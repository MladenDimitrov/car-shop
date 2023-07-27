from django.db import models
from car_shop.account.validators import check_name
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import models as auth_models

# # Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, validators=[check_name, MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, blank=True, null=True, validators=[check_name, MinLengthValidator(1)])

    email = models.EmailField(max_length=40)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='images')
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)


class AppUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'username'
    username = models.CharField(blank=False, null=False, unique=True)
    is_staff = models.BooleanField(default=False)

