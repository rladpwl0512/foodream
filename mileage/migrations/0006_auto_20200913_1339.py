# Generated by Django 3.1 on 2020-09-13 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mileage', '0005_auto_20200913_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mileage',
            name='contents',
            field=models.TextField(null=True),
        ),
    ]
