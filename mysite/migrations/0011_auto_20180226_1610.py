# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-02-26 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20180225_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(default=9901551546),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
