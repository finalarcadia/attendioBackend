# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 08:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendancePK',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 4, 23, 8, 1, 3, 233976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 8, 1, 3, 234006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='class',
            name='ClassPK',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='class',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2016, 4, 23, 8, 1, 3, 232829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='class',
            name='endTime',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 8, 1, 3, 232773, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='class',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2016, 4, 23, 8, 1, 3, 232803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='class',
            name='startTime',
            field=models.TimeField(default=datetime.datetime(2016, 4, 23, 8, 1, 3, 232734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='classrequest',
            name='classRequestPK',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='classroster',
            name='classRosterPK',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='universitydim',
            name='UniversityDimPK',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetaildim',
            name='UserDetailDimPK',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
