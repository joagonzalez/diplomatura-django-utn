# Generated by Django 3.2.5 on 2023-11-28 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_alter_consulta_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]