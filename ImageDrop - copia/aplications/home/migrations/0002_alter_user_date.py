# Generated by Django 4.0.3 on 2022-03-28 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 14, 9, 49, 377004), verbose_name='fecha de registro'),
        ),
    ]
