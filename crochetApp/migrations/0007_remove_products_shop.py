# Generated by Django 3.2 on 2021-05-05 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crochetApp', '0006_products_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='shop',
        ),
    ]