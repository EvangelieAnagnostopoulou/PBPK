# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0027_auto_20141209_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='organ1_params',
            field=models.TextField(max_length=2048, null=True),
            preserve_default=True,
        ),
    ]
