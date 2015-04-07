# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0017_auto_20141121_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='drugs',
            field=models.ManyToManyField(to='pbpk.Drug', blank=True),
            preserve_default=True,
        ),
    ]
