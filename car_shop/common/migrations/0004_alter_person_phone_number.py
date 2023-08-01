# Generated by Django 4.2.3 on 2023-08-01 16:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=10, region=None),
        ),
    ]
