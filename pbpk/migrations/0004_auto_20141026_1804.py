# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0003_auto_20141026_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='bladder_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='bladder_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='blood_bladder_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='blood_kidney_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='blood_liver_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='blood_lung_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='blood_rest_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='blood_skin_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='blood_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='cardiac_output',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='k_bile',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='k_kidney',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='k_met',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='kidney_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='kidney_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='liver_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='liver_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='lung_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='lung_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='max_influx',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='max_kidney',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='max_liver',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='p_bladder',
            field=models.FloatField(default=0.0, null=True, db_column='P_bladder', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='p_kidney',
            field=models.FloatField(default=0.0, null=True, db_column='P_kidney', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='p_liver',
            field=models.FloatField(default=0.0, null=True, db_column='P_liver', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='p_lung',
            field=models.FloatField(default=0.0, null=True, db_column='P_lung', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='p_rest',
            field=models.FloatField(default=0.0, null=True, db_column='P_rest', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='p_skin',
            field=models.FloatField(default=0.0, null=True, db_column='P_skin', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_bladder',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_bladder', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_kidney',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_kidney', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_liver',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_liver', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_lung',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_lung', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_plasma',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_plasma', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_rbc',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_rbc', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_rest',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_rest', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='pi_skin',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_skin', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='skin_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='skin_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
    ]
