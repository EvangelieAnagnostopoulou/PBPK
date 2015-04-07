# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0010_auto_20141107_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='drugname',
        ),
    ]
