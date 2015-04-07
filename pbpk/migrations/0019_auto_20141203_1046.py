# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbpk', '0018_models_drugs'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='max_bladder',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='max_lung',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='max_residual',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='max_skin',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_bladder',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_kidney',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_liver',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_lung',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_residual',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='min_skin',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
