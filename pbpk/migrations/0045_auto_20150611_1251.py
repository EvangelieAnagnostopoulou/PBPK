# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0044_auto_20150203_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='organ1_name',
            field=models.TextField(db_column='organ1Name', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='organ2_name',
            field=models.TextField(db_column='organ2Name', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='organ3_name',
            field=models.TextField(db_column='organ3Name', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='organ4_name',
            field=models.TextField(db_column='organ4Name', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='organ5_name',
            field=models.TextField(db_column='organ5Name', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='models',
            unique_together=set([('username', 'modelname')]),
        ),
    ]
