# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0042_auto_20150120_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_name',
            field=models.TextField(db_column='drugName'),
        ),
        migrations.AlterField(
            model_name='models',
            name='modelname',
            field=models.TextField(db_column='modelName'),
        ),
        migrations.AlterUniqueTogether(
            name='models',
            unique_together=set([('modelname', 'username')]),
        ),
    ]
