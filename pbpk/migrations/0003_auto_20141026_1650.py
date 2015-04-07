# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0002_auto_20141026_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='modelname',
            field=models.TextField(db_column='modelName'),
        ),
        migrations.AlterField(
            model_name='models',
            name='username',
            field=models.TextField(db_column='userName'),
        ),
    ]
