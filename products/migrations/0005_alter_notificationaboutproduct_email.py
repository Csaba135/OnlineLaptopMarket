# Generated by Django 4.0.5 on 2022-07-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options_alter_store_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationaboutproduct',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
