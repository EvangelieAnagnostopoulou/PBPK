# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0020_auto_20141203_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='max_bladder',
            field=models.FloatField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='max_lung',
            field=models.FloatField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='max_residual',
            field=models.FloatField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='max_skin',
            field=models.FloatField(default=1, null=True, blank=True),
        ),
    ]
