# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0012_drug_drug_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_name',
            field=models.TextField(db_column='drugName'),
        ),
    ]
