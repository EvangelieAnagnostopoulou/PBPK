# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0038_auto_20150108_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='plot_params',
            field=models.TextField(null=True, blank=True),
        ),
    ]
