# Generated by Django 4.2.8 on 2023-12-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=1, verbose_name='Остаток'),
        ),
    ]
