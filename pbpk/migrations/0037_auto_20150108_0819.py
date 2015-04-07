# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0036_models_step_params'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='step_params',
            field=models.TextField(max_length=3072, null=True, blank=True),
        ),
    ]
