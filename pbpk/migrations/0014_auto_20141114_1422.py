# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0013_auto_20141107_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='drugs',
            field=models.ManyToManyField(to=b'pbpk.Drug', null=True, blank=True),
        ),
    ]
