# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0019_auto_20171018_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tipo',
            field=models.CharField(choices=[('Consumíveis', 'Consumíveis'), ('Periféricos', 'Periféricos')], default='Consumíveis', max_length=12),
        ),
    ]
