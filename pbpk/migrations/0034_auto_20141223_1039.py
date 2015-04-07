# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0033_auto_20141222_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='max_gut',
            field=models.FloatField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='max_heart',
            field=models.FloatField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='max_muscle',
            field=models.FloatField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='max_placental',
            field=models.FloatField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='max_spleen',
            field=models.FloatField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_gut',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_heart',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_muscle',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_placental',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_spleen',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_placental',
            field=models.FloatField(default=0.0, null=True, db_column='P_placental', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_placental',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_placental', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_placental_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='placental_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='placental_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
