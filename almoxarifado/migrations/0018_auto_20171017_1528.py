# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0017_notebook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notebook',
            old_name='HD',
            new_name='hd',
        ),
    ]
