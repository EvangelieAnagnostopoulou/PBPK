# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0024_auto_20141208_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_name',
            field=models.TextField(db_column='drugName'),
        ),
    ]
