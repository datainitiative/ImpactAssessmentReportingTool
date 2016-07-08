# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'orgnization_stage',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='org_stage',
            field=models.ForeignKey(to='impactassessapp.OrganizationStage', null=True),
        ),
    ]
