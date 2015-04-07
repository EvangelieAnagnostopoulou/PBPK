# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0004_auto_20141026_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='N',
            field=models.IntegerField(default=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='step',
            field=models.FloatField(default=0.0833, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='target',
            field=models.FloatField(default=4e-07, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='total',
            field=models.FloatField(default=4.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
