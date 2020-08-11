# Generated by Django 3.1 on 2020-08-11 09:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0003_auto_20200810_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='stock',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
