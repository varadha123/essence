# Generated by Django 5.0.3 on 2024-03-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
