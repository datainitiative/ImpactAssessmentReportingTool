# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0005_organization_org_stage_note'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='organizationstage',
            table='organization_stage',
        ),
    ]
