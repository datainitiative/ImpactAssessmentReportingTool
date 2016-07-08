# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0004_auto_20160621_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_stage_note',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
