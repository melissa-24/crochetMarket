# Generated by Django 3.2 on 2021-05-05 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crochetApp', '0009_remove_products_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='itemCat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='crochetApp.categories'),
            preserve_default=False,
        ),
    ]