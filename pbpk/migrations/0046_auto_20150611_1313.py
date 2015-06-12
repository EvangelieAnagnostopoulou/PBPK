# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0045_auto_20150611_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='modelname',
            field=models.TextField(db_column='modelName', error_messages={'unique': 'This modelname has already been registered.'}),
        ),
    ]
