# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0010_codebook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codebook',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='indexofquantitativereporting',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='indexofreflectivereporting',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
