# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0029_auto_20141211_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='organ3_params',
            field=models.TextField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='organ4_params',
            field=models.TextField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='organ5_params',
            field=models.TextField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
    ]
