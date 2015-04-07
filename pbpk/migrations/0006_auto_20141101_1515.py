# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0005_auto_20141101_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='N',
            field=models.IntegerField(default=35),
        ),
        migrations.AlterField(
            model_name='models',
            name='step',
            field=models.FloatField(default=0.0833),
        ),
        migrations.AlterField(
            model_name='models',
            name='target',
            field=models.FloatField(default=4e-07),
        ),
        migrations.AlterField(
            model_name='models',
            name='total',
            field=models.FloatField(default=4.0),
        ),
    ]
