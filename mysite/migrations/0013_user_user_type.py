# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-02-27 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_auto_20180227_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default='Customer', max_length=8),
        ),
    ]
