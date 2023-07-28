# Generated by Django 4.2.3 on 2023-07-28 15:46

import car_shop.account.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_person_alter_appuser_managers'),
        ('common', '0002_alter_telephonenumber_telephone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(blank=True, max_length=20, null=True, validators=[car_shop.account.validators.check_name, django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, validators=[car_shop.account.validators.check_name, django.core.validators.MinLengthValidator(1)])),
                ('email', models.EmailField(blank=True, max_length=40, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]