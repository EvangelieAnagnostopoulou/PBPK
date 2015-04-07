# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0039_auto_20150108_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='list_plot',
        ),
    ]
