# Generated by Django 4.0.5 on 2022-07-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_authuser_first_name_alter_authuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nationality',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
