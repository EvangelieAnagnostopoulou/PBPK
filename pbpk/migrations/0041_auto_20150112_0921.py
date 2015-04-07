# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0040_remove_drug_list_plot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='max_gut',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='min_gut',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='p_gut',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='pi_gut',
        ),
        migrations.RemoveField(
            model_name='models',
            name='gut_flow_factor',
        ),
        migrations.RemoveField(
            model_name='models',
            name='gut_volume_fraction',
        ),
    ]
