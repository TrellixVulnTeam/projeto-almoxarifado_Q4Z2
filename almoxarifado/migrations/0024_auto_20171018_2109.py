# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 23:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0023_auto_20171018_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Itens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.Tipo_Itens'),
        ),
    ]
