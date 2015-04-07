# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0006_auto_20141101_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='models',
            old_name='total',
            new_name='end',
        ),
    ]
