# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0031_auto_20141212_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='list_plot',
            field=models.TextField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
    ]
