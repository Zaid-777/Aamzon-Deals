# Generated by Django 3.2.8 on 2021-10-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_remove_products_dealid'),
    ]

    operations = [
        migrations.CreateModel(
            name='chek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
