# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0041_auto_20150112_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='method_params',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='step_params',
            field=models.TextField(null=True, blank=True),
        ),
    ]
