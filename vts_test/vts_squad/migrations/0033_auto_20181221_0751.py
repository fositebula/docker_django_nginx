# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-21 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vts_squad', '0032_job_download_compress_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jenkins_job',
            field=models.CharField(default='', max_length=64),
        ),
    ]
