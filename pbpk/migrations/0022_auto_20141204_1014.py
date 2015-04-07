# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0021_auto_20141204_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='p_organ1',
            field=models.FloatField(default=0.0, null=True, db_column='P_organ1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_organ2',
            field=models.FloatField(default=0.0, null=True, db_column='P_organ2', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_organ3',
            field=models.FloatField(default=0.0, null=True, db_column='P_organ3', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_organ4',
            field=models.FloatField(default=0.0, null=True, db_column='P_organ4', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_organ5',
            field=models.FloatField(default=0.0, null=True, db_column='P_organ5', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_organ1',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_organ1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_organ2',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_organ2', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_organ3',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_organ3', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_organ4',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_organ4', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_organ5',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_organ5', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_organ1_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_organ2_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_organ3_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_organ4_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_organ5_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ1_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ1_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ2_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ2_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ3_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ3_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ4_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ4_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ5_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='organ5_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
