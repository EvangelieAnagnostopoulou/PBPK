# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0043_auto_20150203_0855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='models',
            unique_together=None,
        ),
    ]
