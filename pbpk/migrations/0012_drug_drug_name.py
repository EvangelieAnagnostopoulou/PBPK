# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0011_remove_drug_drugname'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='drug_name',
            field=models.TextField(default='drug1', db_column='drugName'),
            preserve_default=True,
        ),
    ]
