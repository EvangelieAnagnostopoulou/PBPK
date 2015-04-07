# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0023_auto_20141208_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='models',
            name='organ1name',
        ),
        migrations.RemoveField(
            model_name='models',
            name='organ2name',
        ),
        migrations.RemoveField(
            model_name='models',
            name='organ3name',
        ),
        migrations.RemoveField(
            model_name='models',
            name='organ4name',
        ),
        migrations.RemoveField(
            model_name='models',
            name='organ5name',
        ),
        migrations.AddField(
            model_name='models',
            name='organ1_name',
            field=models.TextField(default='organ name', db_column='organ1Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ2_name',
            field=models.TextField(default='organ name', db_column='organ2Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ3_name',
            field=models.TextField(default='organ name', db_column='organ3Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ4_name',
            field=models.TextField(default='organ name', db_column='organ4Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ5_name',
            field=models.TextField(default='organ name', db_column='organ5Name', blank=True),
            preserve_default=True,
        ),
    ]
