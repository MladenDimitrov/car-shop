# Generated by Django 4.2.3 on 2023-08-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_specifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
