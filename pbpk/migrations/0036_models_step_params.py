# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0035_models_plot_params'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='step_params',
            field=models.TextField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
    ]
