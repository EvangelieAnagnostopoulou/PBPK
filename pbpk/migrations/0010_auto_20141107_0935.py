# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0009_auto_20141107_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drugname',
            field=models.TextField(null=True, db_column='drugName', blank=True),
        ),
    ]
