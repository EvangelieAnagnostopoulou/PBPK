# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0034_auto_20141223_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='plot_params',
            field=models.TextField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
    ]
