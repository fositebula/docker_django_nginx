# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-11 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=1024)),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenkins_job', models.CharField(default='', max_length=32)),
                ('jenkins_build_num', models.CharField(default='', max_length=12)),
                ('jenkins_node', models.CharField(default='', max_length=12)),
                ('jenkins_trigger', models.CharField(default='', max_length=12)),
                ('jenkins_build_type', models.CharField(default='', max_length=8)),
                ('jenkins_lavatest', models.CharField(default='', max_length=8)),
                ('jenkins_changes', models.CharField(default='', max_length=256)),
                ('jenkins_sync_code_interval', models.CharField(default='', max_length=256)),
                ('jenkins_build_interval', models.CharField(default='', max_length=256)),
                ('jenkins_pac_interval', models.CharField(default='', max_length=256)),
                ('lava_job', models.CharField(default='', max_length=32)),
                ('lava_job_status', models.CharField(default='Submitted', max_length=8)),
                ('lava_job_log', models.TextField(default='', max_length=1048576)),
                ('lava_job_yaml', models.TextField(default='', max_length=5120)),
                ('submit_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VtsModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vtsmodule', models.CharField(max_length=128)),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='YamlTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('templates', models.TextField(default='', max_length=5120)),
                ('description', models.CharField(default='', max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='yamltemplate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vts_squad.YamlTemplate'),
        ),
        migrations.AddField(
            model_name='comment',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vts_squad.Job'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vts_squad.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
