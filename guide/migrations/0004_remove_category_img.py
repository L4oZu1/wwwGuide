# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_auto_20170811_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='img',
        ),
    ]
