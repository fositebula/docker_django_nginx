# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-12 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vts_squad', '0003_lavadevicetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='lavadevicetype',
            name='pac_url',
            field=models.CharField(default='', max_length=256),
        ),
    ]
