# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0008_auto_20160726_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='cost_effectiveness',
            field=models.ForeignKey(to='impactassessapp.CostEffectiveness', null=True),
        ),
    ]
