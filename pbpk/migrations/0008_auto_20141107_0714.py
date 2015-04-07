# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0007_auto_20141101_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('drugname', models.TextField(db_column='drugName')),
                ('k_met', models.FloatField(default=0.0, null=True, blank=True)),
                ('k_bile', models.FloatField(default=0.0, null=True, blank=True)),
                ('k_kidney', models.FloatField(default=0.0, null=True, blank=True)),
                ('max_liver', models.FloatField(default=0.0, null=True, blank=True)),
                ('max_kidney', models.FloatField(default=0.0, null=True, blank=True)),
                ('max_influx', models.FloatField(default=0.0, null=True, blank=True)),
                ('p_skin', models.FloatField(default=0.0, null=True, db_column='P_skin', blank=True)),
                ('pi_skin', models.FloatField(default=0.0, null=True, db_column='Pi_skin', blank=True)),
                ('p_kidney', models.FloatField(default=0.0, null=True, db_column='P_kidney', blank=True)),
                ('pi_kidney', models.FloatField(default=0.0, null=True, db_column='Pi_kidney', blank=True)),
                ('p_bladder', models.FloatField(default=0.0, null=True, db_column='P_bladder', blank=True)),
                ('pi_bladder', models.FloatField(default=0.0, null=True, db_column='Pi_bladder', blank=True)),
                ('p_rest', models.FloatField(default=0.0, null=True, db_column='P_rest', blank=True)),
                ('pi_rest', models.FloatField(default=0.0, null=True, db_column='Pi_rest', blank=True)),
                ('p_liver', models.FloatField(default=0.0, null=True, db_column='P_liver', blank=True)),
                ('pi_liver', models.FloatField(default=0.0, null=True, db_column='Pi_liver', blank=True)),
                ('pi_rbc', models.FloatField(default=0.0, null=True, db_column='Pi_rbc', blank=True)),
                ('pi_plasma', models.FloatField(default=0.0, null=True, db_column='Pi_plasma', blank=True)),
                ('p_lung', models.FloatField(default=0.0, null=True, db_column='P_lung', blank=True)),
                ('pi_lung', models.FloatField(default=0.0, null=True, db_column='Pi_lung', blank=True)),
            ],
            options={
                'db_table': 'drugs',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='models',
            name='k_bile',
        ),
        migrations.RemoveField(
            model_name='models',
            name='k_kidney',
        ),
        migrations.RemoveField(
            model_name='models',
            name='k_met',
        ),
        migrations.RemoveField(
            model_name='models',
            name='max_influx',
        ),
        migrations.RemoveField(
            model_name='models',
            name='max_kidney',
        ),
        migrations.RemoveField(
            model_name='models',
            name='max_liver',
        ),
        migrations.RemoveField(
            model_name='models',
            name='p_bladder',
        ),
        migrations.RemoveField(
            model_name='models',
            name='p_kidney',
        ),
        migrations.RemoveField(
            model_name='models',
            name='p_liver',
        ),
        migrations.RemoveField(
            model_name='models',
            name='p_lung',
        ),
        migrations.RemoveField(
            model_name='models',
            name='p_rest',
        ),
        migrations.RemoveField(
            model_name='models',
            name='p_skin',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_bladder',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_kidney',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_liver',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_lung',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_plasma',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_rbc',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_rest',
        ),
        migrations.RemoveField(
            model_name='models',
            name='pi_skin',
        ),
        migrations.AddField(
            model_name='models',
            name='drugs',
            field=models.ManyToManyField(to='pbpk.Drug'),
            preserve_default=True,
        ),
    ]
