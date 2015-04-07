# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0028_drug_organ1_params'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='organ2_params',
            field=models.TextField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='drug',
            name='organ1_params',
            field=models.TextField(max_length=2048, null=True, blank=True),
        ),
    ]
