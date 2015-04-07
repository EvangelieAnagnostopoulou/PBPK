# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.TextField(db_column='userName', blank=True)),
                ('modelname', models.TextField(db_column='modelName', blank=True)),
                ('bw', models.FloatField(null=True, blank=True)),
                ('h', models.FloatField(null=True, blank=True)),
                ('cardiac_output', models.FloatField(null=True, blank=True)),
                ('k_met', models.FloatField(null=True, blank=True)),
                ('k_bile', models.FloatField(null=True, blank=True)),
                ('k_kidney', models.FloatField(null=True, blank=True)),
                ('max_liver', models.FloatField(null=True, blank=True)),
                ('max_kidney', models.FloatField(null=True, blank=True)),
                ('max_influx', models.FloatField(null=True, blank=True)),
                ('skin_flow_factor', models.FloatField(null=True, blank=True)),
                ('skin_volume_fraction', models.FloatField(null=True, blank=True)),
                ('blood_skin_fraction', models.FloatField(null=True, blank=True)),
                ('p_skin', models.FloatField(null=True, db_column='P_skin', blank=True)),
                ('pi_skin', models.FloatField(null=True, db_column='Pi_skin', blank=True)),
                ('kidney_flow_factor', models.FloatField(null=True, blank=True)),
                ('kidney_volume_fraction', models.FloatField(null=True, blank=True)),
                ('blood_kidney_fraction', models.FloatField(null=True, blank=True)),
                ('p_kidney', models.FloatField(null=True, db_column='P_kidney', blank=True)),
                ('pi_kidney', models.FloatField(null=True, db_column='Pi_kidney', blank=True)),
                ('bladder_flow_factor', models.FloatField(null=True, blank=True)),
                ('bladder_volume_fraction', models.FloatField(null=True, blank=True)),
                ('blood_bladder_fraction', models.FloatField(null=True, blank=True)),
                ('p_bladder', models.FloatField(null=True, db_column='P_bladder', blank=True)),
                ('pi_bladder', models.FloatField(null=True, db_column='Pi_bladder', blank=True)),
                ('blood_rest_fraction', models.FloatField(null=True, blank=True)),
                ('p_rest', models.FloatField(null=True, db_column='P_rest', blank=True)),
                ('pi_rest', models.FloatField(null=True, db_column='Pi_rest', blank=True)),
                ('liver_flow_factor', models.FloatField(null=True, blank=True)),
                ('liver_volume_fraction', models.FloatField(null=True, blank=True)),
                ('blood_liver_fraction', models.FloatField(null=True, blank=True)),
                ('p_liver', models.FloatField(null=True, db_column='P_liver', blank=True)),
                ('pi_liver', models.FloatField(null=True, db_column='Pi_liver', blank=True)),
                ('blood_volume_fraction', models.FloatField(null=True, blank=True)),
                ('pi_rbc', models.FloatField(null=True, db_column='Pi_rbc', blank=True)),
                ('pi_plasma', models.FloatField(null=True, db_column='Pi_plasma', blank=True)),
                ('lung_flow_factor', models.FloatField(null=True, blank=True)),
                ('lung_volume_fraction', models.FloatField(null=True, blank=True)),
                ('blood_lung_fraction', models.FloatField(null=True, blank=True)),
                ('p_lung', models.FloatField(null=True, db_column='P_lung', blank=True)),
                ('pi_lung', models.FloatField(null=True, db_column='Pi_lung', blank=True)),
            ],
            options={
                'db_table': 'models',
            },
            bases=(models.Model,),
        ),
    ]
