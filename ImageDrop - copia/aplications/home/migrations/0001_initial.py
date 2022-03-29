# Generated by Django 4.0.3 on 2022-03-28 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('dni', models.CharField(max_length=15, verbose_name='Cedula')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Foto/%Y/%M/%D')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 28, 14, 7, 21, 675599), verbose_name='fecha de registro')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'User',
                'ordering': ['id'],
            },
        ),
    ]
