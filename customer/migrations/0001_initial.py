# Generated by Django 5.0.3 on 2024-03-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100, null=True)),
                ('Email', models.TextField(max_length=100, null=True)),
                ('Password', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
