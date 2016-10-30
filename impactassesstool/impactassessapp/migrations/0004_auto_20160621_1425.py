# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0003_auto_20160621_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='amount_note',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='beneficiary_level_indicator',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='organization_level_indicator',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='recommended_indicator',
            field=models.TextField(null=True, blank=True),
        ),
    ]
