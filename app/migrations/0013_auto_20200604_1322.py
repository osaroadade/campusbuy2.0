# Generated by Django 3.0.3 on 2020-06-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]