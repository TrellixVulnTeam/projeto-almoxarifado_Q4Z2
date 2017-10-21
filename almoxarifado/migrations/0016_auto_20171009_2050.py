# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0015_auto_20171009_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='item',
            name='cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
