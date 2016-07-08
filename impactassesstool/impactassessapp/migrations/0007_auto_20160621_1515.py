# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0006_auto_20160621_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
