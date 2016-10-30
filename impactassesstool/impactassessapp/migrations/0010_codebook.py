# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impactassessapp', '0009_investment_cost_effectiveness'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('source', models.TextField(max_length=500, null=True, blank=True)),
                ('comments', models.TextField(max_length=500, null=True, blank=True)),
                ('data_type_for_database', models.CharField(max_length=200, null=True, blank=True)),
                ('notes_on_initial_database', models.TextField(max_length=500, null=True, blank=True)),
                ('model_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'codebook',
            },
        ),
    ]
