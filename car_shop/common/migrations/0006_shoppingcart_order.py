# Generated by Django 4.2.3 on 2023-08-07 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_testmodel'),
        ('common', '0005_alter_person_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm_purchase_of_product', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PN', 'Pending'), ('PR', 'Processing order'), ('PT', 'Pending tracking event'), ('TR', 'Tracking Info Received'), ('IT', 'In transit'), ('OD', 'Out for delivery'), ('DE', 'Delivered')], default='PN')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region='BG')),
                ('total_price', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
