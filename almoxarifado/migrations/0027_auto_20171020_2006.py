# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0026_auto_20171018_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricante',
            name='fabricante',
            field=models.CharField(max_length=90, unique=True),
        ),
    ]
