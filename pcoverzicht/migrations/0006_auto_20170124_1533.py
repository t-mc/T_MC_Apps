# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcoverzicht', '0005_auto_20170124_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='merkentype',
            field=models.CharField(max_length=80, verbose_name='Merk en Type'),
        ),
        migrations.AlterField(
            model_name='software',
            name='productkey',
            field=models.CharField(max_length=40, null=True),
        ),
    ]