# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0022_auto_20141204_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='organ1name',
            field=models.TextField(default='', db_column='organ1Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ2name',
            field=models.TextField(default='', db_column='organ2Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ3name',
            field=models.TextField(default='', db_column='organ3Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ4name',
            field=models.TextField(default='', db_column='organ4Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ5name',
            field=models.TextField(default='', db_column='organ5Name', blank=True),
            preserve_default=True,
        ),
    ]
