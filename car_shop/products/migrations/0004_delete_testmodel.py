# Generated by Django 4.2.3 on 2023-08-10 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_testmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]