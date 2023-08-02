# Generated by Django 4.2.3 on 2023-08-01 16:12

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_person_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=13, region='BG'),
        ),
    ]