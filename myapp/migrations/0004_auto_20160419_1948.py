# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160419_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='code',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='class',
            name='codeExpirationDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='class',
            name='codeFlag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='class',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='class',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]