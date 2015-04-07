# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0032_drug_list_plot'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='p_gut',
            field=models.FloatField(default=0.0, null=True, db_column='P_gut', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_heart',
            field=models.FloatField(default=0.0, null=True, db_column='P_heart', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_muscle',
            field=models.FloatField(default=0.0, null=True, db_column='P_muscle', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='p_spleen',
            field=models.FloatField(default=0.0, null=True, db_column='P_spleen', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_gut',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_gut', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_heart',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_heart', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_muscle',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_muscle', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='pi_spleen',
            field=models.FloatField(default=0.0, null=True, db_column='Pi_spleen', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_gut_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_heart_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_muscle_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='blood_spleen_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='gut_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='gut_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='heart_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='heart_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='muscle_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='muscle_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='spleen_flow_factor',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='models',
            name='spleen_volume_fraction',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
