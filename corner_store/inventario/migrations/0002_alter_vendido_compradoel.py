# Generated by Django 4.1.3 on 2022-11-30 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendido',
            name='compradoEl',
            field=models.DateField(default=datetime.datetime(2022, 11, 30, 21, 9, 18, 994717)),
        ),
    ]
