# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0016_auto_20141114_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='models',
            name='N',
        ),
        migrations.RemoveField(
            model_name='models',
            name='drugs',
        ),
        migrations.RemoveField(
            model_name='models',
            name='end',
        ),
        migrations.RemoveField(
            model_name='models',
            name='step',
        ),
        migrations.RemoveField(
            model_name='models',
            name='target',
        ),
        migrations.AddField(
            model_name='models',
            name='method',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='method_params',
            field=models.TextField(max_length=2048, null=True),
            preserve_default=True,
        ),
    ]
