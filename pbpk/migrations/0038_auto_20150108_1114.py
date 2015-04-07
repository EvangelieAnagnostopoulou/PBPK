# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0037_auto_20150108_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='plot_params',
            field=models.TextField(max_length=40960, null=True, blank=True),
        ),
    ]
