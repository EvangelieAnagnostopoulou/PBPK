# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0014_auto_20141114_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='drugs',
            field=models.ManyToManyField(to=b'pbpk.Drug', blank=True),
        ),
    ]
