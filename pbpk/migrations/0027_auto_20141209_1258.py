# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0026_auto_20141209_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_name',
            field=models.TextField(unique=True, db_column='drugName'),
        ),
    ]
