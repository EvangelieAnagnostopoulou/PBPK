# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0030_auto_20141211_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='organ2_params',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='organ3_params',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='organ4_params',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='organ5_params',
        ),
    ]
